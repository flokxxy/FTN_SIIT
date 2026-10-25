package com.example.demo.service;

import com.example.demo.exception.NotFoundException;
import com.example.demo.model.Accommodation;
import com.example.demo.model.DateRange;
import com.example.demo.repository.AccommodationRepository;

public class AccommodationServiceImpl implements AccommodationService {

    private final AccommodationRepository repository;

    public AccommodationServiceImpl(AccommodationRepository repository) {
        this.repository = repository;
    }

    @Override
    public void save(Accommodation accommodation) {
        repository.save(accommodation);
    }

    @Override
    public Accommodation getById(long accommodationId) {
        return repository.findById(accommodationId)
                .orElseThrow(() -> new NotFoundException(String.format("Accommodation with ID %s not found.", accommodationId)));
    }

    @Override
    public boolean isAccommodationAvailable(long accommodationId, DateRange dateRange) {
        Accommodation accommodation = getById(accommodationId);

        if (dateRange.getStartDate().isBefore(accommodation.getAvailability().getStartDate()) ||
                dateRange.getEndDate().isAfter(accommodation.getAvailability().getEndDate())) {
            return false;
        }

        return accommodation.getReservations().stream()
                .noneMatch(existingReservation ->
                        !existingReservation.getEndDate().isBefore(dateRange.getStartDate()) &&
                                !existingReservation.getStartDate().isAfter(dateRange.getEndDate())
                );
    }

    @Override
    public Accommodation getByReservationId(long reservationId) {
        return repository.findByReservationId(reservationId)
                .orElseThrow(() -> new NotFoundException(String.format("Accommodation with reservation ID %s not found.", reservationId)));
    }
}
