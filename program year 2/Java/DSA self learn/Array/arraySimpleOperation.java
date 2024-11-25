package Array;

public class arraySimpleOperation {

    //search operation
    static int findElement(int arr[], int x){
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == x){
                return i;
            }
        }
        return -1;
    }


    //insert operation (end)
    static int[] insertElementAtTheEnd(int arr[] ,int e){
        //int n = arr.length;
        int newarr[] = new int[arr.length + 1];

        for(int i = 0; i<arr.length; i++){
            newarr[i] = arr[i];
        }
        newarr[arr.length] = e;
        return newarr;
    }


    //insert operation (any position)
    static int[] insertElementAnywhere(int arr[], int index, int element){
        int newarr[] = new int[arr.length+1];

        for(int i = 0; i < index; i++){
            newarr[i] = arr[i];
        }

        for(int i = arr.length-1; i >= index; i--){
            newarr[i+1] = arr[i];
        }
        newarr[index] = element;

        return newarr;
    }


    //delete element
    static int[] deleteElement(int arr[], int element){
        int newarr[] = new int[arr.length-1];

        int pos = findElement(arr, element);
        for(int i = arr.length-1; i >= pos; i--){
            newarr[i-1] = arr[i];
        }
        for(int i = 0; i < pos; i++){
            newarr[i] = arr[i];
        }
        return newarr;
    }


    //binary search (sorted array)
    static int BinarySearch(int arr[], int x){
        int left = 0;
        int right = arr.length - 1;
        int mid = left + right / 2;
        while (left < right){
            if (mid == x){
                return mid;
            }
            else if (mid < x){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    //reverse an array
    static int[] ReverseArray(int arr[]){
        int[] newarr = new int[arr.length];
        for (int i = 0; i < arr.length; i++){
            newarr[i] = arr[arr.length - 1 - i];
        }
        return newarr;
    }




    public static void main(String[] args) {
        int arr[] = { 12, 34, 10, 6, 40 };

        //search opearion usage
//        int x = findElement(arr, 10);
//        System.out.println(x);


        //insert (end) operation
//        int newarr[] = insertElementAtTheEnd(arr, 69);
//        for(int i = 0; i < newarr.length; i++){
//            System.out.println(newarr[i]);
//        }

        //insert (any) operation
//        int newarr[] = insertElementAnywhere(arr, 2,69);
//        for(int i = 0; i < newarr.length; i++){
//            System.out.println(newarr[i]);
//        }

        //delete element
        int newarr[] = deleteElement(arr, 10);
        for(int i = 0; i < newarr.length; i++){
            System.out.println(newarr[i]);
        }
    }
}
