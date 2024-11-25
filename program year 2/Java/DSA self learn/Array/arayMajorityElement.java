package Array;
import java.util.HashMap;
import java.util.Map;

public class arayMajorityElement {


    static int MajorityElement(int[] arr){
        Map<Integer, Integer> countMap = new HashMap<>();

        for(int i = 0;i < arr.length; i++){
            countMap.put(arr[i], countMap.getOrDefault(arr[i], 0) + 1);

            if (countMap.get(arr[i]) > arr.length / 2) {
                return arr[i];
            }
        }
        return -1;

    }
    public static void main(String[] args) {
        int[] arr = {2, 3, 2, 2, 3, 5, 2};
        System.out.println(MajorityElement(arr));
    }
}
