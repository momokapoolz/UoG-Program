package com.example.adminyogaappcw;


import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.adminyogaappcw.model.yogaClass;

public class ConfirmYogaClassActivity extends AppCompatActivity {

    private TextView txtSummary;
    private Button btnConfirmSave, btnEdit;

    private yogaClass yc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_confirm_yoga_class);

        txtSummary = findViewById(R.id.txtClassDetails);
        btnConfirmSave = findViewById(R.id.btnConfirmSave);
        btnEdit = findViewById(R.id.btnEdit);

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
                AddYogaClassActivity tempActivity = new AddYogaClassActivity();

                tempActivity.saveToLocal(ConfirmYogaClassActivity.this, yc);
                tempActivity.saveToFirebase(yc);

                Toast.makeText(this, "Saved to local & Firebase!", Toast.LENGTH_SHORT).show();
                finish();
            }
        });

        btnEdit.setText("Edit");
        btnEdit.setOnClickListener(v -> {
            onBackPressed(); // Quay lại màn trước
        });
    }
}
