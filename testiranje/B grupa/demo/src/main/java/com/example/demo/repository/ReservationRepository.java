package com.example.demo.repository;

import com.example.demo.model.Reservation;

import java.util.List;
import java.util.Optional;

public interface ReservationRepository {

    Optional<Reservation> findById(long reservationId);

    List<Reservation> findAllByClientId(long clientId);

    void save(Reservation reservation);

    void delete(Reservation reservation);
}
