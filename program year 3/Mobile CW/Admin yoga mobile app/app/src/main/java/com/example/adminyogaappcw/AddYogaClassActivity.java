package com.example.adminyogaappcw;


import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

import com.example.adminyogaappcw.db.DatabaseHelper;
import com.example.adminyogaappcw.model.yogaClass;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class AddYogaClassActivity extends AppCompatActivity {

    private EditText edtDay, edtTime, edtCapacity, edtDuration, edtPrice, edtType, edtDescription, edtInstructor, edtDifficulty;
    private Button btnSubmit, btnHome;
    private TextView txtError;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_yoga_class);

        edtDay = findViewById(R.id.edtDay);
        edtTime = findViewById(R.id.edtTime);
        edtCapacity = findViewById(R.id.edtCapacity);
        edtDuration = findViewById(R.id.edtDuration);
        edtPrice = findViewById(R.id.edtPrice);
        edtType = findViewById(R.id.edtType);
        edtDescription = findViewById(R.id.edtDescription);
        edtInstructor = findViewById(R.id.edtInstructor);
        edtDifficulty = findViewById(R.id.edtDifficulty);
        btnSubmit = findViewById(R.id.btnSubmit);
        btnHome = findViewById(R.id.btnHome);
        txtError = findViewById(R.id.txtError);

        btnSubmit.setOnClickListener(view -> {
            String day = edtDay.getText().toString().trim();
            String time = edtTime.getText().toString().trim();
            String capacityStr = edtCapacity.getText().toString().trim();
            String durationStr = edtDuration.getText().toString().trim();
            String priceStr = edtPrice.getText().toString().trim();
            String type = edtType.getText().toString().trim();
            String description = edtDescription.getText().toString().trim();
            String instructor = edtInstructor.getText().toString().trim();
            String difficulty = edtDifficulty.getText().toString().trim();

            // Validate required fields
            if (day.isEmpty() || time.isEmpty() || capacityStr.isEmpty() ||
                    durationStr.isEmpty() || priceStr.isEmpty() || type.isEmpty()) {
                txtError.setText("Please fill in all required fields.");
                return;
            }

            try {
                int capacity = Integer.parseInt(capacityStr);
                int duration = Integer.parseInt(durationStr);
                double price = Double.parseDouble(priceStr);

                yogaClass newClass = new yogaClass(day, time, capacity, duration, price, type,
                        description, instructor, difficulty);

                Intent intent = new Intent(AddYogaClassActivity.this, ConfirmYogaClassActivity.class);
                intent.putExtra("yogaClass", newClass);
                startActivity(intent);
            } catch (NumberFormatException e) {
                txtError.setText("Invalid number format.");
            }
        });
        
        btnHome.setOnClickListener(view -> {
            Intent intent = new Intent(AddYogaClassActivity.this, MainActivity.class);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
            startActivity(intent);
        });
    }

    // === Save to SQLite ===
    public void saveToLocal(Context context, yogaClass yogaClass) {
        DatabaseHelper dbHelper = new DatabaseHelper(context);
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        ContentValues values = new ContentValues();
        values.put(DatabaseHelper.COL_DAY, yogaClass.getDayOfWeek());
        values.put(DatabaseHelper.COL_TIME, yogaClass.getTime());
        values.put(DatabaseHelper.COL_CAPACITY, yogaClass.getCapacity());
        values.put(DatabaseHelper.COL_DURATION, yogaClass.getDurationMinutes());
        values.put(DatabaseHelper.COL_PRICE, yogaClass.getPrice());
        values.put(DatabaseHelper.COL_TYPE, yogaClass.getType());
        values.put(DatabaseHelper.COL_DESCRIPTION, yogaClass.getDescription());
        values.put(DatabaseHelper.COL_INSTRUCTOR, yogaClass.getInstructorName());
        values.put(DatabaseHelper.COL_DIFFICULTY, yogaClass.getDifficultyLevel());

        long result = db.insert(DatabaseHelper.TABLE_YOGA, null, values);
        db.close();

        if (result != -1) {
            Toast.makeText(context, "Saved locally", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(context, "Failed to save locally", Toast.LENGTH_SHORT).show();
        }
    }

    // === Save to Firebase Realtime Database ===
    public void saveToFirebase(yogaClass yogaClass) {
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference ref = database.getReference("yoga_classes");

        String key = ref.push().getKey();
        if (key != null) {
            ref.child(key).setValue(yogaClass)
                    .addOnSuccessListener(unused ->
                            Toast.makeText(this, "Saved to Firebase", Toast.LENGTH_SHORT).show())
                    .addOnFailureListener(e ->
                            Toast.makeText(this, "Firebase Error: " + e.getMessage(), Toast.LENGTH_SHORT).show());
        }
    }
}
