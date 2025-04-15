package com.example.adminyogaappcw.db;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {

    public static final String DATABASE_NAME = "yoga.db";
    public static final int DATABASE_VERSION = 1;

    public static final String TABLE_YOGA = "yoga_class";
    public static final String COL_ID = "id";
    public static final String COL_DAY = "day_of_week";
    public static final String COL_TIME = "time";
    public static final String COL_CAPACITY = "capacity";
    public static final String COL_DURATION = "duration_minutes";
    public static final String COL_PRICE = "price";
    public static final String COL_TYPE = "type";
    public static final String COL_DESCRIPTION = "description";
    public static final String COL_INSTRUCTOR = "instructor_name";
    public static final String COL_DIFFICULTY = "difficulty_level";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createTable = "CREATE TABLE " + TABLE_YOGA + " (" +
                COL_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                COL_DAY + " TEXT, " +
                COL_TIME + " TEXT, " +
                COL_CAPACITY + " INTEGER, " +
                COL_DURATION + " INTEGER, " +
                COL_PRICE + " REAL, " +
                COL_TYPE + " TEXT, " +
                COL_DESCRIPTION + " TEXT, " +
                COL_INSTRUCTOR + " TEXT, " +
                COL_DIFFICULTY + " TEXT)";
        db.execSQL(createTable);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_YOGA);
        onCreate(db);
    }
}
