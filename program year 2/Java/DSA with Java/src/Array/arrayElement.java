package Array;
import java.util.Arrays;

public class arrayElement {
    public static void main(String[] args) {

        int[] arr = {1,2,3,4};
        int newIndex = 2;
        int newEle = 0;
        int[] newArr = addElementToArray(arr, newIndex, newEle);


        for (int element: newArr) {
            System.out.println(element);
        }

        int brr[] = {9,2,13,4,5};
        int crr[] =  {1,2,3};
        brr = Arrays.copyOf(crr, crr.length);
        System.out.println(brr.toString());

    }

    public static int[] addElementToArray(int[] arr, int newIndex, int newEle){
        int[] newArr = new int[arr.length + 1];
        for(int i = 0; i < arr.length; i++){
            if(i < newIndex){
                newArr[i] = arr[i];
            } else if (i == newIndex){
                newArr[i] = newEle;
            } else{
                newArr[i] = arr[i-1];
            }
        }
        return newArr;
    }
}
