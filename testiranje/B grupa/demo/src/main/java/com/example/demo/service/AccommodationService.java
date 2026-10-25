package com.example.demo.service;

import com.example.demo.model.Accommodation;
import com.example.demo.model.DateRange;

public interface AccommodationService {

    void save(Accommodation accommodation);

    Accommodation getById(long accommodationId);

    boolean isAccommodationAvailable(long accommodationId, DateRange dateRange);

    Accommodation getByReservationId(long reservationId);
}

