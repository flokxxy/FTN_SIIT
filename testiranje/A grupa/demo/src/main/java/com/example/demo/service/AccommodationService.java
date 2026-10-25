package com.example.demo.service;

import com.example.demo.exception.NotFoundException;
import com.example.demo.model.Accommodation;
import com.example.demo.model.DateRange;
import com.example.demo.model.Reservation;
import com.example.demo.repository.AccommodationRepository;

import java.util.List;

public class AccommodationService {

    private final AccommodationRepository repository;

    public AccommodationService(AccommodationRepository repository) {
        this.repository = repository;
    }

    public Accommodation getById(long id) {
        return repository.findById(id)
                .orElseThrow(() -> new NotFoundException(String.format("Accommodation with ID %s not found..", id)));
    }

    public boolean isAccommodationAvailable(long accommodationId, DateRange dateRange) {
        Accommodation accommodation = getById(accommodationId);

        boolean isInAvailabilityPeriod = isDateRangeWithinAvailability(dateRange, accommodation.getAvailability());
        boolean hasOverlappingReservations = hasOverlappingReservations(accommodation.getReservations(), dateRange);

        return isInAvailabilityPeriod && !hasOverlappingReservations;
    }

    private boolean isDateRangeWithinAvailability(DateRange dateRange, DateRange availability) {
        return availability.getStartDate().isBefore(dateRange.getStartDate())
                && availability.getEndDate().isAfter(dateRange.getEndDate());
    }

    private boolean hasOverlappingReservations(List<Reservation> reservations, DateRange dateRange) {
        return reservations.stream()
                .anyMatch(reservation ->
                        !reservation.getEndDate().isBefore(dateRange.getStartDate()) &&
                                !reservation.getStartDate().isAfter(dateRange.getEndDate()));
    }

    public void save(Accommodation accommodation) {
        repository.save(accommodation);
    }
}

