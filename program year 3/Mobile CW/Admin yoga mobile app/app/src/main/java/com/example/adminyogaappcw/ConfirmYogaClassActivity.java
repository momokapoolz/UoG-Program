package com.example.adminyogaappcw;


import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.adminyogaappcw.db.DatabaseHelper;
import com.example.adminyogaappcw.model.yogaClass;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class ConfirmYogaClassActivity extends AppCompatActivity {

    private TextView txtSummary;
    private Button btnConfirmSave, btnEdit, btnHome;

    private yogaClass yc;
    private DatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_confirm_yoga_class);

        txtSummary = findViewById(R.id.txtClassDetails);
        btnConfirmSave = findViewById(R.id.btnConfirmSave);
        btnEdit = findViewById(R.id.btnEdit);
        btnHome = findViewById(R.id.btnHome);
        dbHelper = new DatabaseHelper(this);

        yc = (yogaClass) getIntent().getSerializableExtra("yogaClass");

        if (yc != null) {
            String summary = "Day: " + yc.getDayOfWeek() + "\n"
                    + "Time: " + yc.getTime() + "\n"
                    + "Capacity: " + yc.getCapacity() + "\n"
                    + "Duration: " + yc.getDurationMinutes() + " minutes\n"
                    + "Price: $" + yc.getPrice() + "\n"
                    + "Type: " + yc.getType() + "\n"
                    + "Description: " + yc.getDescription() + "\n"
                    + "Instructor: " + yc.getInstructorName() + "\n"
                    + "Difficulty: " + yc.getDifficultyLevel();

            txtSummary.setText(summary);
        }

        btnConfirmSave.setText("Confirm & Save");
        btnConfirmSave.setOnClickListener(v -> {
            if (yc != null) {
                // Save to local SQLite database
                long result = dbHelper.addYogaClass(yc);
                
                if (result != -1) {
                    Toast.makeText(this, "Saved to local database", Toast.LENGTH_SHORT).show();
                    
                    // Save to Firebase
                    saveToFirebase(yc);
                } else {
                    Toast.makeText(this, "Failed to save to local database", Toast.LENGTH_SHORT).show();
                }
                
                finish();
            }
        });

        btnEdit.setText("Edit");
        btnEdit.setOnClickListener(v -> {
            onBackPressed(); // Go back to previous screen
        });
        
        btnHome.setOnClickListener(v -> {
            Intent intent = new Intent(this, MainActivity.class);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
            startActivity(intent);
        });
    }
    
    // Save to Firebase Realtime Database
    private void saveToFirebase(yogaClass yogaClass) {
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
