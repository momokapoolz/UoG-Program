package Array;
import java.util.Scanner;
import java.util.Arrays;


public class sortArrFrom1toN {

    public static void sortArrFrom1toN(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            int correct = arr[i] - 1;
            if (arr[i] != correct) {
                swap(arr, i, correct);
            } else {
                i++;
            }
        }
    }
    



    public static void main(String[] args) {
        int[] arr = { 3, 2, 5, 6, 1, 4 };

        // Function call
        sortArrFrom1toN(arr);

        // Printing the answer
        System.out.println(Arrays.toString(arr));
    }
    
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
