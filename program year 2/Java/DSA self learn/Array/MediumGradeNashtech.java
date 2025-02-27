package Array;

import java.util.Scanner;
import java.util.ArrayList;


public class MediumGradeNashtech {

    // Function to calculate the MG for a class
    public static double calculateMG(ArrayList<ArrayList<Integer>> scores) {
        double totalAverageScore = 0.0;
        int numberOfStudents = scores.size();

        for (ArrayList<Integer> studentScores : scores) {
            double studentTotal = 0.0;
            for (int score : studentScores) {
                studentTotal += score;
            }
            double studentAverage = studentTotal / studentScores.size(); // Average for each student
            totalAverageScore += studentAverage;
        }

        return totalAverageScore / numberOfStudents; // Return the Medium Grade (MG)
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the scores in the format [[10,9,8,7],[10,8,7,6],...]:");
        String input = scanner.nextLine();

        // Parse the input into a nested ArrayList
        ArrayList<ArrayList<Integer>> scores = new ArrayList<>();
        input = input.replaceAll("\\[\\[", "").replaceAll("\\]\\]", "");
        String[] students = input.split("\\],\\[");

        for (String student : students) {
            ArrayList<Integer> studentScores = new ArrayList<>();
            for (String score : student.split(",")) {
                studentScores.add(Integer.parseInt(score.trim()));
            }
            scores.add(studentScores);
        }

        // Call the function and calculate MG
        double MG = calculateMG(scores);

        System.out.printf("Medium Grade (MG): %.2f%n", MG);

        scanner.close();
    }
}
