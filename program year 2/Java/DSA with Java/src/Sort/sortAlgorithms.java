package Sort;

import java.util.Arrays;

public class sortAlgorithms {
    public static void main(String[] args) {
        int arr[] = {2,4,5,3,6,8,7};
        //int brr[] = selectionSort(arr);
        int crr[] = bubbleSort(arr);
        System.out.print("sorted: " + Arrays.toString(crr));
    }

    public static int[] selectionSort(int[] arr) {
        /*
        tim index cua min trong arr va swap cho index 0
         */

        //tim min
        for (int i = 0; i < arr.length-1; i++)
        {
            // Find the minimum element in unsorted array
            int min_idx = i;
            for (int j = i+1; j < arr.length; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;

            // Swap the found minimum element with the first element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }

        return arr;
    }



    //bubblesort
    public static int[] bubbleSort(int[] arr){
        boolean swapped = false;
        for(int i = 0; i<arr.length;i++){ //loop i tu cuoi len dau
            for(int j = 0; j<i-1; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return arr;
    }


    //quick sort
    /*
    pick a random element, send it to middle and do the same with left and right side of it
    * */

    /*
    public static int[] quockSort(){

    }

    public int partition(int[] arr, int left, int right boolean asc){
        int pivot = arr[right];
        int i = left - 1;
        //chon 1 phan tu (de ten la pivot) sau do dua cac phan tu < pivot ve ben trai, >pivot ve ben phai
    }

     */
}
