package org.example;

public class Work {
        private String JobTitle;
        private String JobType;
        private String companyN;
        private int time_work;
        private double stavka;

    public Work(String jobTitle, String jobType, String companyN, int time_work, double stavka) {
        this.JobTitle = jobTitle;
        this.JobType = jobType;
        this.companyN = companyN;
        this.time_work = time_work;
        this.stavka = stavka;
    }

    public String getJobTitle() {
        return JobTitle;
    }

    public String getJobType() {
        return JobType;
    }

    public String getCompanyN() {
        return companyN;
    }


    public int getTime_work() {
        return time_work;
    }
    public double getStavka(){
        return stavka;
    }

    public double getInWork(){
        return stavka * time_work;
    }


}
