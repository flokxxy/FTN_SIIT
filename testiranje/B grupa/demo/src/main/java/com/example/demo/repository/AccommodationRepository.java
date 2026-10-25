package com.example.demo.repository;

import com.example.demo.model.Accommodation;

import java.util.Optional;

public interface AccommodationRepository {

    void save(Accommodation accommodation);

    Optional<Accommodation> findById(long accommodationId);

    Optional<Accommodation> findByReservationId(long reservationId);
}
