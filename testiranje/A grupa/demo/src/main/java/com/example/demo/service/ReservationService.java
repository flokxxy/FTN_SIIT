package com.example.demo.service;

import com.example.demo.model.Accommodation;
import com.example.demo.model.Client;
import com.example.demo.model.DateRange;
import com.example.demo.model.Reservation;
import com.example.demo.repository.ReservationRepository;

import java.util.List;

public class ReservationService {

    private final ReservationRepository repository;

    private final AccommodationService accommodationService;

    public ReservationService(ReservationRepository repository, AccommodationService accommodationService) {
        this.repository = repository;
        this.accommodationService = accommodationService;
    }

    /**
     * A GRUPA
     *
     * Metoda koja pravi rezervaciju tako sto prvo proveri
     * da li su validni datumi za koje se pravi rezervacija,
     * zatim proveri da li je smestaj slobodan u tom periodu
     * i da li je klijent slobodan u tom periodu
     *
     * @param accommodationId id smestaja
     * @param client klijent koji zeli da napravi rezervaciju
     * @param dateRange period u kojem zeli da rezervise smestaj
     * @return da li je rezervacija napravljena
     */
    public boolean createReservation(long accommodationId, Client client, DateRange dateRange) {

        if (dateRange.getStartDate().isAfter(dateRange.getEndDate())) {
            throw new IllegalArgumentException("Invalid date range: Start date is after end date.");
        }

        if (!accommodationService.isAccommodationAvailable(accommodationId, dateRange)) {
            return false;
        }

        if(clientHasReservations(client.getId(), dateRange)){
            return false;
        }

        Reservation reservation = new Reservation(client, dateRange.getStartDate(), dateRange.getEndDate());
        repository.save(reservation);
        Accommodation accommodation = accommodationService.getById(accommodationId);
        accommodation.getReservations().add(reservation);
        accommodationService.save(accommodation);
        return true;
    }

    private boolean clientHasReservations(long clientId, DateRange dateRange) {
        List<Reservation> existingReservations = repository.findAllByClientId(clientId);
        boolean hasOverlappingReservations = existingReservations.stream()
                .anyMatch(reservation ->
                        !reservation.getEndDate().isBefore(dateRange.getStartDate()) &&
                                !reservation.getStartDate().isAfter(dateRange.getEndDate()));
        return hasOverlappingReservations;
    }
}

