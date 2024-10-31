package org.example;

public class Departure {
    String routeCode;
    String departurePlace;
    String arrivalPlace;
    String departureDate;
    String departureTime;
    String arrivalTime;
    String platform;
    double ticketPrice;
    int ticketsSold;

    public String getRouteCode() { return routeCode; }
    public String getDeparturePlace() { return departurePlace; }
    public String getArrivalPlace() { return arrivalPlace; }
    public String getDepartureDate() { return departureDate; }
    public String getDepartureTime() { return departureTime; }
    public String getArrivalTime() { return arrivalTime; }
    public String getPlatform() { return platform; }
    public double getTicketPrice() { return ticketPrice; }
    public int getTicketsSold() { return ticketsSold; }


    public Departure(String routeCode, String departurePlace, String arrivalPlace, String departureDate,
                     String departureTime, String arrivalTime, String platform, double ticketPrice, int ticketsSold) {
        this.routeCode = routeCode;
        this.departurePlace = departurePlace;
        this.arrivalPlace = arrivalPlace;
        this.departureDate = departureDate;
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.platform = platform;
        this.ticketPrice = ticketPrice;
        this.ticketsSold = ticketsSold;
    }
}
