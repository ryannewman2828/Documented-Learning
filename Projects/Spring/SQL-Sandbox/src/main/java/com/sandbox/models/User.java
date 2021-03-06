package com.sandbox.models;

public class User {

    private int id;
    private String name;
    private String email;
    private int salary;
    private int grade;
    private boolean pass;
    private String fields;
    private int sum;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public int getGrade() {
        return grade;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    public boolean isPass() {
        return pass;
    }

    public void setPass(boolean pass) {
        this.pass = pass;
    }

    public String getFields() { return fields; }

    public void setFields(String fields) {
        this.fields = fields;
    }

    public int getSum() { return sum; }

    public void setSum(int sum) { this.sum = sum; }
}
