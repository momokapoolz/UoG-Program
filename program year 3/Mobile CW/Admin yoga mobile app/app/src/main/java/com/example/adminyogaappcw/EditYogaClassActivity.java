package com.example.adminyogaappcw;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.example.adminyogaappcw.db.DatabaseHelper;
import com.example.adminyogaappcw.model.yogaClass;

public class EditYogaClassActivity extends AppCompatActivity {

    private EditText edtDay, edtTime, edtCapacity, edtDuration, edtPrice, edtType, edtDescription, edtInstructor, edtDifficulty;
    private Button btnUpdate, btnDelete, btnHome;
    private TextView txtError;
    private DatabaseHelper dbHelper;
    private yogaClass currentClass;
    private String originalDay, originalTime;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_yoga_class);

        // Initialize UI components
        edtDay = findViewById(R.id.edtDay);
        edtTime = findViewById(R.id.edtTime);
        edtCapacity = findViewById(R.id.edtCapacity);
        edtDuration = findViewById(R.id.edtDuration);
        edtPrice = findViewById(R.id.edtPrice);
        edtType = findViewById(R.id.edtType);
        edtDescription = findViewById(R.id.edtDescription);
        edtInstructor = findViewById(R.id.edtInstructor);
        edtDifficulty = findViewById(R.id.edtDifficulty);
        btnUpdate = findViewById(R.id.btnUpdate);
        btnDelete = findViewById(R.id.btnDelete);
        btnHome = findViewById(R.id.btnHome);
        txtError = findViewById(R.id.txtError);
        
        dbHelper = new DatabaseHelper(this);
        
        // Get yoga class from intent
        if (getIntent().hasExtra("yogaClass")) {
            currentClass = (yogaClass) getIntent().getSerializableExtra("yogaClass");
            populateFields(currentClass);
            originalDay = currentClass.getDayOfWeek();
            originalTime = currentClass.getTime();
        }
        
        // Update button click handler
        btnUpdate.setOnClickListener(v -> {
            if (validateInputs()) {
                yogaClass updatedClass = getYogaClassFromInputs();
                boolean success = dbHelper.updateYogaClass(originalDay, originalTime, updatedClass);
                
                if (success) {
                    Toast.makeText(this, "Class updated successfully", Toast.LENGTH_SHORT).show();
                    finish();
                } else {
                    Toast.makeText(this, "Failed to update class", Toast.LENGTH_SHORT).show();
                }
            }
        });
        
        // Delete button click handler
        btnDelete.setOnClickListener(v -> {
            new AlertDialog.Builder(this)
                .setTitle("Delete Yoga Class")
                .setMessage("Are you sure you want to delete this class?")
                .setPositiveButton("Yes", (dialog, which) -> {
                    dbHelper.deleteYogaClass(currentClass);
                    Toast.makeText(this, "Class deleted successfully", Toast.LENGTH_SHORT).show();
                    finish();
                })
                .setNegativeButton("No", null)
                .show();
        });
        
        // Home button click handler
        btnHome.setOnClickListener(v -> {
            Intent intent = new Intent(this, MainActivity.class);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
            startActivity(intent);
        });
    }
    
    private void populateFields(yogaClass yc) {
        edtDay.setText(yc.getDayOfWeek());
        edtTime.setText(yc.getTime());
        edtCapacity.setText(String.valueOf(yc.getCapacity()));
        edtDuration.setText(String.valueOf(yc.getDurationMinutes()));
        edtPrice.setText(String.valueOf(yc.getPrice()));
        edtType.setText(yc.getType());
        edtDescription.setText(yc.getDescription());
        edtInstructor.setText(yc.getInstructorName());
        edtDifficulty.setText(yc.getDifficultyLevel());
    }
    
    private boolean validateInputs() {
        String day = edtDay.getText().toString().trim();
        String time = edtTime.getText().toString().trim();
        String capacityStr = edtCapacity.getText().toString().trim();
        String durationStr = edtDuration.getText().toString().trim();
        String priceStr = edtPrice.getText().toString().trim();
        String type = edtType.getText().toString().trim();
        
        // Check required fields
        if (day.isEmpty() || time.isEmpty() || capacityStr.isEmpty() ||
                durationStr.isEmpty() || priceStr.isEmpty() || type.isEmpty()) {
            txtError.setText("Please fill in all required fields");
            return false;
        }
        
        // Validate numeric fields
        try {
            Integer.parseInt(capacityStr);
            Integer.parseInt(durationStr);
            Double.parseDouble(priceStr);
        } catch (NumberFormatException e) {
            txtError.setText("Invalid number format");
            return false;
        }
        
        return true;
    }
    
    private yogaClass getYogaClassFromInputs() {
        String day = edtDay.getText().toString().trim();
        String time = edtTime.getText().toString().trim();
        int capacity = Integer.parseInt(edtCapacity.getText().toString().trim());
        int duration = Integer.parseInt(edtDuration.getText().toString().trim());
        double price = Double.parseDouble(edtPrice.getText().toString().trim());
        String type = edtType.getText().toString().trim();
        String description = edtDescription.getText().toString().trim();
        String instructor = edtInstructor.getText().toString().trim();
        String difficulty = edtDifficulty.getText().toString().trim();
        
        return new yogaClass(day, time, capacity, duration, price, type, description, instructor, difficulty);
    }
} 