package Array;

public class arrayPairOfSum {

    static boolean binarySearch(int[] arr, int x){
        int left = 0;
        int right = arr.length - 1;



        while(left <= right){
            int mid = (left + right) / 2;
            if(arr[mid] == x){
                return true;
            }
            else if (arr[mid] < x){
                left = mid+1;
            } else{
                right = mid-1;
            }
        }
        return false;
    }



    static boolean twoSum(int[] arr, int target){
        for(int i = 0; i < arr.length; i++){
            int ideal_target = target - arr[i];
            if (binarySearch(arr, ideal_target)){
                return true;
            }
        }
        return false;
    }



    public static void main(String[] args) {
        //sorted array cho nhanh ae
        int[] arr = {1,2,3,4,5};

        boolean result = twoSum(arr, 8);
        System.out.println(result);
    }
}
