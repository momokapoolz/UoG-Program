package com.example.adminyogaappcw.model;

public class yogaClass {
    private String dayOfWeek;
    private String time;
    private int capacity;
    private int durationMinutes;
    private double price;
    private String type;
    private String description;
    private String instructorName; // additional field
    private String difficultyLevel; // additional field: Beginner, Intermediate, Advanced

    public yogaClass() {}

    public yogaClass(String dayOfWeek, String time, int capacity, int durationMinutes, double price,
                     String type, String description, String instructorName, String difficultyLevel) {
        this.dayOfWeek = dayOfWeek;
        this.time = time;
        this.capacity = capacity;
        this.durationMinutes = durationMinutes;
        this.price = price;
        this.type = type;
        this.description = description;
        this.instructorName = instructorName;
        this.difficultyLevel = difficultyLevel;
    }

    // Getters and setters...
    public String getDayOfWeek() { return dayOfWeek; }
    public String getTime() { return time; }
    public int getCapacity() { return capacity; }
    public int getDurationMinutes() { return durationMinutes; }
    public double getPrice() { return price; }
    public String getType() { return type; }
    public String getDescription() { return description; }
    public String getInstructorName() { return instructorName; }
    public String getDifficultyLevel() { return difficultyLevel; }
}

