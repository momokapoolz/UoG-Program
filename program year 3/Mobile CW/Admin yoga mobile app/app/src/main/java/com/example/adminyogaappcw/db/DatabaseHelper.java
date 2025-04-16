package com.example.adminyogaappcw.db;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.widget.Toast;

import com.example.adminyogaappcw.model.yogaClass;

import java.util.ArrayList;

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


    public ArrayList<yogaClass> getAllYogaClasses() {
        ArrayList<yogaClass> list = new ArrayList<>();
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.query(TABLE_YOGA, null, null, null, null, null, null);
        while (cursor.moveToNext()) {
            yogaClass yc = new yogaClass(
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_DAY)),
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_TIME)),
                    cursor.getInt(cursor.getColumnIndexOrThrow(COL_CAPACITY)),
                    cursor.getInt(cursor.getColumnIndexOrThrow(COL_DURATION)),
                    cursor.getDouble(cursor.getColumnIndexOrThrow(COL_PRICE)),
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_TYPE)),
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_DESCRIPTION)),
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_INSTRUCTOR)),
                    cursor.getString(cursor.getColumnIndexOrThrow(COL_DIFFICULTY))
            );
            list.add(yc);
        }
        cursor.close();
        db.close();
        return list;
    }

    public void deleteYogaClass(yogaClass yogaClass) {
        SQLiteDatabase db = this.getWritableDatabase();
        db.delete(TABLE_YOGA, COL_DAY + "=? AND " + COL_TIME + "=?",
                new String[]{yogaClass.getDayOfWeek(), yogaClass.getTime()});
        db.close();
    }
    
    public boolean updateYogaClass(String originalDay, String originalTime, yogaClass updatedClass) {
        SQLiteDatabase db = this.getWritableDatabase();
        
        ContentValues values = new ContentValues();
        values.put(COL_DAY, updatedClass.getDayOfWeek());
        values.put(COL_TIME, updatedClass.getTime());
        values.put(COL_CAPACITY, updatedClass.getCapacity());
        values.put(COL_DURATION, updatedClass.getDurationMinutes());
        values.put(COL_PRICE, updatedClass.getPrice());
        values.put(COL_TYPE, updatedClass.getType());
        values.put(COL_DESCRIPTION, updatedClass.getDescription());
        values.put(COL_INSTRUCTOR, updatedClass.getInstructorName());
        values.put(COL_DIFFICULTY, updatedClass.getDifficultyLevel());
        
        int rowsAffected = db.update(TABLE_YOGA, values, 
                COL_DAY + "=? AND " + COL_TIME + "=?", 
                new String[]{originalDay, originalTime});
        
        db.close();
        return rowsAffected > 0;
    }
    
    public long addYogaClass(yogaClass yogaClass) {
        SQLiteDatabase db = this.getWritableDatabase();
        
        ContentValues values = new ContentValues();
        values.put(COL_DAY, yogaClass.getDayOfWeek());
        values.put(COL_TIME, yogaClass.getTime());
        values.put(COL_CAPACITY, yogaClass.getCapacity());
        values.put(COL_DURATION, yogaClass.getDurationMinutes());
        values.put(COL_PRICE, yogaClass.getPrice());
        values.put(COL_TYPE, yogaClass.getType());
        values.put(COL_DESCRIPTION, yogaClass.getDescription());
        values.put(COL_INSTRUCTOR, yogaClass.getInstructorName());
        values.put(COL_DIFFICULTY, yogaClass.getDifficultyLevel());
        
        long result = db.insert(TABLE_YOGA, null, values);
        db.close();
        
        return result;
    }
}
