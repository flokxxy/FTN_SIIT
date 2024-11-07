package org.example;

public class Company {
    private String Name;
    private int sr_hours;
    private double dohod;
    private int hours_of_w;
    private int works;

    public Company(String Name){
        this.Name = Name;
    }

    public void addWork(Work work){
        this.dohod += work.getInWork();
        this.hours_of_w += work.getTime_work();
        if ("Name".equalsIgnoreCase(work.getJobType())){
            this.sr_hours += work.getTime_work();
        }
        this.works++;
    }

    public String getName() {
        return Name;
    }

    public int getSr_hours() {
        return sr_hours;
    }

    public double getDohod() {
        return dohod;
    }

    public int getHours_of_w() {
        return hours_of_w;
    }

    public double getSrHours(){
        return works > 0 ? (double) hours_of_w/works : 0;
    }

    @Override
    public String toString() {
        return String.format("Total Income: %.2f, " +
                        "Total Hours: %d, " +
                        "Repair Hours: %d, " +
                        "Average Hours: %.2f",
                Name, sr_hours,dohod,hours_of_w,getSrHours());



    }
}
