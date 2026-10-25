package com.example.demo.model;

import java.util.List;

public class Accommodation {

    private long id;

    private String location;

    private DateRange availability;

    private List<Reservation> reservations;

    public Accommodation(long id, String location, DateRange availability, List<Reservation> reservations) {
        this.id = id;
        this.location = location;
        this.availability = availability;
        this.reservations = reservations;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public DateRange getAvailability() {
        return availability;
    }

    public void setAvailability(DateRange availability) {
        this.availability = availability;
    }

    public List<Reservation> getReservations() {
        return reservations;
    }

    public void setReservations(List<Reservation> reservations) {
        this.reservations = reservations;
    }
}
