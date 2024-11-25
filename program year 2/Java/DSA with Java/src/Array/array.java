package Array;

import java.util.Arrays;

public class array {
    public static void main(String[] args) {

        int[] arr = {1, 2, 3, 4, 5};

        System.out.println(Arrays.toString(arr));
        //Lenght of array = capacity: sức chứa của mảng

        //Scanner sc = new Scanner(System.in);

//        for(int i = 0; i < arr.length; i++){
//            arr[i] = sc.nextInt();
//        }

//        int[] rev = reverseArrayC1(arr);
//
//        System.out.println(Arrays.toString(rev));
//
//        int[] rev2 = reverseArrayC2(arr);
//
//        System.out.println(Arrays.toString(rev2));

          search(6, arr);
    }

    public static int[] reverseArrayC1(int[] arr){

        for(int i = 0; i < arr.length/2; i++){
            int temp = arr[i];
            arr[i] = arr[arr.length - i - 1];
            arr[arr.length - i - 1] = temp;
        }

        return arr;
    }

    public static int[] reverseArrayC2(int[] arr){
        int[] rev = new int[arr.length];

        for(int i = 0; i < rev.length ; i++){
            rev[rev.length - i - 1] = arr[i];
        }

        return rev;
    }

    public static void search(int key, int[] arr){
        boolean found = false;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == key){
                System.out.println("found at " + i);
                found = true;
            }
        }
        if(found == false){
            System.out.println("ko thay ni");
        }

    }


    public static int findLocation(int key, int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) {
                return i;
            }
        }
        return -1;
    }
}
