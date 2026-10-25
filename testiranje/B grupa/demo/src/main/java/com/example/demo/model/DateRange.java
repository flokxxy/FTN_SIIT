package com.example.demo.model;

import java.time.LocalDate;

public class DateRange {

    private LocalDate startDate;

    private LocalDate endDate;

    public DateRange(LocalDate from, LocalDate to) {
        this.startDate = from;
        this.endDate = to;
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
