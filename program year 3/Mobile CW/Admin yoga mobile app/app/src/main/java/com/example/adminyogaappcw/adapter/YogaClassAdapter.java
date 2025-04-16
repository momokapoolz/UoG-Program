package com.example.adminyogaappcw.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.example.adminyogaappcw.R;
import com.example.adminyogaappcw.model.yogaClass;

import java.util.ArrayList;

public class YogaClassAdapter extends ArrayAdapter<yogaClass> {
    private Context context;
    private ArrayList<yogaClass> classes;

    public YogaClassAdapter(Context context, ArrayList<yogaClass> classes) {
        super(context, R.layout.item_yoga_class, classes);
        this.context = context;
        this.classes = classes;
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View listItem = convertView;
        if (listItem == null) {
            listItem = LayoutInflater.from(context).inflate(R.layout.item_yoga_class, parent, false);
        }

        yogaClass currentClass = classes.get(position);

        TextView txtDay = listItem.findViewById(R.id.txtDay);
        TextView txtTime = listItem.findViewById(R.id.txtTime);
        TextView txtType = listItem.findViewById(R.id.txtType);
        TextView txtDifficulty = listItem.findViewById(R.id.txtDifficulty);
        TextView txtInstructor = listItem.findViewById(R.id.txtInstructor);
        TextView txtPrice = listItem.findViewById(R.id.txtPrice);
        TextView txtDuration = listItem.findViewById(R.id.txtDuration);

        txtDay.setText(currentClass.getDayOfWeek());
        txtTime.setText(currentClass.getTime());
        txtType.setText(currentClass.getType());
        txtDifficulty.setText(currentClass.getDifficultyLevel());
        txtInstructor.setText(currentClass.getInstructorName());
        txtPrice.setText(String.format("$%.2f", currentClass.getPrice()));
        txtDuration.setText(String.format("%d mins", currentClass.getDurationMinutes()));

        return listItem;
    }
} 