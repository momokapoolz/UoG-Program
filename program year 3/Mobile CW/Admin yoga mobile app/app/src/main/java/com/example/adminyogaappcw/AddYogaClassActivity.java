package com.example.adminyogaappcw;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import com.example.adminyogaappcw.R;
import com.example.adminyogaappcw.model.yogaClass;

public class AddYogaClassActivity extends AppCompatActivity {

    private EditText edtDay, edtTime, edtCapacity, edtDuration, edtPrice, edtType, edtDescription, edtInstructor, edtDifficulty;
    private Button btnSubmit;
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

            if (day.isEmpty() || time.isEmpty() || capacityStr.isEmpty() || durationStr.isEmpty()
                    || priceStr.isEmpty() || type.isEmpty()) {
                txtError.setText("Please fill in all required fields.");
                return;
            }

            int capacity = Integer.parseInt(capacityStr);
            int duration = Integer.parseInt(durationStr);
            double price = Double.parseDouble(priceStr);

            yogaClass newClass = new yogaClass(day, time, capacity, duration, price, type, description, instructor, difficulty);

            Intent intent = new Intent(AddYogaClassActivity.this, ConfirmYogaClassActivity.class);
            intent.putExtra("yogaClass", newClass);
            startActivity(intent);
        });
    }
}
