package com.example.demo.repository;

import com.example.demo.model.Reservation;

import java.util.List;

public interface ReservationRepository {

    List<Reservation> findAllByClientId(long clientId);

    void save(Reservation reservation);
}
