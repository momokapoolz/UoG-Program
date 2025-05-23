package com.example.adminyogaappcw;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import com.example.adminyogaappcw.R;

public class MainActivity extends AppCompatActivity {

    private Button btnAddClass;
    private Button btnViewClasses;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnAddClass = findViewById(R.id.btnAddClass);
        btnViewClasses = findViewById(R.id.btnViewClasses);
        
        btnAddClass.setOnClickListener(view -> {
            Intent intent = new Intent(MainActivity.this, AddYogaClassActivity.class);
            startActivity(intent);
        });
        
        btnViewClasses.setOnClickListener(view -> {
            Intent intent = new Intent(MainActivity.this, ListYogaClassesActivity.class);
            startActivity(intent);
        });
    }
}
