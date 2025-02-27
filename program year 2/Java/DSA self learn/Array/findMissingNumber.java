package Array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class findMissingNumber {

    public static void findMissingNumberNaive(int[] arr) {
        int n = arr.length + 1;
        int[] hash = new int[n+1];

        for(int i = 0; i < arr.length; i++){
            hash[arr[i]]++;
        }


        for(int i = 1; i <= hash.length - 1; i++){
            if (hash[i] == 0){
                System.out.println(i);
            }
        }
    }




    public static void main(String[] args) {
        int arr[] = {1,2,3,5};

        findMissingNumberNaive(arr);

    }
}
