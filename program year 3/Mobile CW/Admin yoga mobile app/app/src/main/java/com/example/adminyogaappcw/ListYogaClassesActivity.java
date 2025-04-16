package com.example.adminyogaappcw;

import android.content.Intent;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

import com.example.adminyogaappcw.adapter.YogaClassAdapter;
import com.example.adminyogaappcw.db.DatabaseHelper;
import com.example.adminyogaappcw.model.yogaClass;

import java.util.ArrayList;

public class ListYogaClassesActivity extends AppCompatActivity {

    ListView listView;
    Button btnAddNew, btnHome;
    YogaClassAdapter adapter;
    ArrayList<yogaClass> classList;
    DatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_yoga_classes);

        listView = findViewById(R.id.listViewYogaClasses);
        btnAddNew = findViewById(R.id.btnAddNew);
        btnHome = findViewById(R.id.btnHome);
        dbHelper = new DatabaseHelper(this);
        
        btnAddNew.setOnClickListener(v -> {
            Intent intent = new Intent(this, AddYogaClassActivity.class);
            startActivity(intent);
        });
        
        btnHome.setOnClickListener(v -> {
            Intent intent = new Intent(this, MainActivity.class);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
            startActivity(intent);
        });

        listView.setOnItemClickListener((adapterView, view, i, l) -> {
            yogaClass selected = classList.get(i);
            Intent intent = new Intent(this, EditYogaClassActivity.class);
            intent.putExtra("yogaClass", selected);
            startActivity(intent);
        });
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        loadData();
    }

    private void loadData() {
        classList = dbHelper.getAllYogaClasses();
        adapter = new YogaClassAdapter(this, classList);
        listView.setAdapter(adapter);
        
        if (classList.isEmpty()) {
            Toast.makeText(this, "No yoga classes found", Toast.LENGTH_SHORT).show();
        }
    }
}
