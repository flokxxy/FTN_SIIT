package com.example.demo.service;

import com.example.demo.exception.NotFoundException;
import com.example.demo.model.Accommodation;
import com.example.demo.model.Client;
import com.example.demo.model.DateRange;
import com.example.demo.model.Reservation;
import com.example.demo.repository.ReservationRepository;
import com.example.demo.util.DateTimeProvider;

import java.time.LocalDate;
import java.util.List;

public class ReservationService {

    private final ReservationRepository repository;

    private final AccommodationService accommodationService;

    private final DateTimeProvider dateTimeProvider;

    public ReservationService(ReservationRepository repository, AccommodationService accommodationService) {
        this(repository, accommodationService, new DateTimeProvider());
    }

    public ReservationService(ReservationRepository repository, AccommodationService accommodationService, DateTimeProvider dateTimeProvider) {
        this.repository = repository;
        this.accommodationService = accommodationService;
        this.dateTimeProvider = dateTimeProvider;
    }

    /**
     * B GRUPA
     *
     * Metoda koja otkazuje rezervaciju ako rezervacija postoji,
     * ako ta rezervacija pripada klijentu koji zeli da je otkaze
     * i ako je moguce otkazati rezervaciju
     *
     * Rezervaciju je moguce otkazati ako traje 2 dana ili manje
     * ili ako traje vise od 2 dana, a nije prosao rok za otkazivanje rezervacije
     *
     * rok za otkazivanje rezervacije je 5 dana pre pocetka
     *
     * @param reservationId id rezervacije koju klijent zeli da otkaze
     * @param client klijent koji zeli da otkaze rezervaciju
     * @return da li je rezervacija otkazana
     */
    public boolean cancelReservation(long reservationId, Client client) {

        Reservation reservation = repository.findById(reservationId)
                .orElseThrow(() -> new NotFoundException(String.format("Reservation with ID %s not found.", reservationId)));

        if(reservation.getClient().getId() != client.getId()) {
            throw new IllegalStateException("Only the client who made the reservation can cancel.");
        }

        if(!isPossibleToCancelReservation(reservation)) {
            return false;
        }

        repository.delete(reservation);
        Accommodation accommodation = accommodationService.getByReservationId(reservationId);
        accommodation.getReservations().remove(reservation);
        accommodationService.save(accommodation);
        return true;
    }

    public boolean createReservation(long accommodationId, Client client, DateRange dateRange) {
        if (dateRange.getStartDate().isAfter(dateRange.getEndDate())) {
            throw new IllegalArgumentException("Start date must not be after end date.");
        }

        if (!accommodationService.isAccommodationAvailable(accommodationId, dateRange)) {
            return false;
        }

        List<Reservation> existingReservations = repository.findAllByClientId(client.getId());
        boolean hasOverlap = existingReservations.stream()
                .anyMatch(existingReservation ->
                        !existingReservation.getEndDate().isBefore(dateRange.getStartDate()) &&
                        !existingReservation.getStartDate().isAfter(dateRange.getEndDate())
                );

        if (hasOverlap) {
            return false;
        }

        Accommodation accommodation = accommodationService.getById(accommodationId);
        Reservation reservation = new Reservation(client, dateRange.getStartDate(), dateRange.getEndDate());
        repository.save(reservation);
        accommodation.getReservations().add(reservation);
        accommodationService.save(accommodation);

        return true;
    }

    private boolean isPossibleToCancelReservation(Reservation reservation) {
        LocalDate currentTime = dateTimeProvider.getCurrentTime();
        if (currentTime.isAfter(reservation.getStartDate())) {
            throw new IllegalStateException("Reservation has already started.");
        }
        long duration = reservation.getStartDate().datesUntil(reservation.getEndDate()).count();
        long days = currentTime.datesUntil(reservation.getStartDate()).count();
        return duration <= 2 || days >= 5;
    }
}

