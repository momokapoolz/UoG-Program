package Array;
import java.util.ArrayList;

//if an element is larger that it's right, it considered a "leader"
public class arrayLeader {

    //nested loop
    static void leaderArray(int[] arr) {
        for(int i=0; i < arr.length; i++){
            int j;
            for(j = i + 1; j < arr.length; j++){
                if(arr[i] <= arr[j]){
                    break;
                }
            }

            if (j == arr.length){
                System.out.println(arr[i]);
            }
        }
    }


    //one loop
    static void leaderArrayLessComplex(int[] arr){
        int leader = arr[arr.length - 1];

        for(int i = arr.length - 2; i >=0; i--){
            if(arr[i] > leader){
                leader = arr[i];
                System.out.println(leader);
            }
        }
    }



    public static void main(String[] args) {
        int arr[] = { 16, 17, 4, 3, 5, 2 };
        leaderArray(arr);
        leaderArrayLessComplex(arr);
    }
}
