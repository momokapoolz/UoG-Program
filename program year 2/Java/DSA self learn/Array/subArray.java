package Array;
import java.util.Arrays;


public class subArray {


    //Subarray la mang con cua 1 array gom cac phan tu LIEN KE nhau
    static int maxSubarraySumNaiveApproach(int[] arr){
        int result = arr[0];
        for(int i = 0; i < arr.length; i++){
            int currentSum = 0;
            for(int j = i; j < arr.length; j++){
                currentSum = currentSum + arr[j];

                // Update result if currentSum > result
                result = Math.max(result, currentSum);
            }
        }
        return result;
    }

    static int maxSubarraySumKadane(int[] arr) {
        int res = arr[0];
        int maxEnding = arr[0];

        for (int i = 1; i < arr.length; i++) {

            // Find the maximum sum ending at index i by either extending
            // the maximum sum subarray ending at index i - 1 or by
            // starting a new subarray from index i
            maxEnding = Math.max(maxEnding + arr[i], arr[i]);

            // Update res if maximum subarray sum ending at index i > res
            res = Math.max(res, maxEnding);
        }
        return res;
    }

    public static void main(String[] args) {

    }
}
