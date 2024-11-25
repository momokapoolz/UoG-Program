package Sort;

public class checkIfSorted {
    public static void main(String[] args) {
        int[] arr = {1,2,5,4};
        checkSorted(arr);

        int isSorted = checkSorted_TheoCachCuaThay(arr);
        System.out.println(isSorted);
    }


    public static void checkSorted(int[] arr){
        int countASC = 0;
        int countDESC = 0;
        for(int i = 0; i < arr.length-1; i++){
            if(arr[i] < arr[i+1]){
                countASC+=1;
            } else if (arr[i] > arr[i+1]){
                countDESC+=1;
            }
        }
        if (countASC == arr.length - 1){
            System.out.println("Sorted from small to big");
        } else if (countDESC == arr.length - 1) {
            System.out.println("Sorted from big to small");
        } else{
            System.out.println("Unsorted");
        }
    }



    public static int checkSorted_TheoCachCuaThay(int[] arr){
        boolean asc = true;
        boolean desc = true;
        for(int i=0; i<arr.length-1; i++){
            if(arr[i] > arr[i+1]){
                asc = false;
                break;
            }
        }
        for(int i=0; i<arr.length-1; i++){
            if(arr[i] < arr[i+1]){
                desc = false;
                break;
            }
        }

        if(asc){
            return 1;
        } else if (desc) {
            return 0;
        } else {
            return -1;
        }
    }



}
