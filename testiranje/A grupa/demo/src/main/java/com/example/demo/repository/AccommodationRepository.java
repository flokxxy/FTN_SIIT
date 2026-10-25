package com.example.demo.repository;

import com.example.demo.model.Accommodation;

import java.util.Optional;

public interface AccommodationRepository {

    Optional<Accommodation> findById(long id);

    void save(Accommodation accommodation);
}
