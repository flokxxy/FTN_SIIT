package com.example.demo.model;

import java.time.LocalDate;

public class Reservation {

    private long id;

    private Client client;

    private LocalDate startDate;

    private LocalDate endDate;

    public Reservation(long id, Client client, LocalDate startDate, LocalDate endDate) {
        this.id = id;
        this.client = client;
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public Reservation(Client client, LocalDate startDate, LocalDate endDate) {
        this.client = client;
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public LocalDate getEndDate() {
        return endDate;
    }

    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }
}
