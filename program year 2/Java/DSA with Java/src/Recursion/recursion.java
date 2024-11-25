package Recursion;

import java.util.Arrays;

public class recursion {
    public static void main(String[] args) {
        int a = tinhTongCacSoChantu_a_den_b(1, 11);
        System.out.println(a);

        int[] arr = {1,4,3,6,2,9,5,8,7,10};

        reverseUsingRecusrion(arr, 0, arr.length-1);

        System.out.println(Arrays.toString(arr));
    }

    public static int tinhTongTu1DenNcach1(int n){
        //ap dung cont thuc gauss
        int sum = n*(n+1)/2;
        return sum;
    }



    public static int tinhTongTu1DenNcach2(int n) {
        //dung pp lap for
        int sum = 0;
        for (int i = 0; i <= n; i++) {
            sum = sum + i;
        }
        return sum;
    }



    public static int tinhTongTu1DenNcach2nhmaDungChoArray(int[] n) {
        //dung pp lap for nhma dung cho array
        int sum = 0;
        for (int i = 0; i <= n.length; i++) {
            sum = sum + n[i];
        }
        return sum;
    }



    public static int tinhTongTu1DenNcach3_DeQuy(int n){
        if (n == 1){
            return 1;
        } else {
            return tinhTongTu1DenNcach3_DeQuy(n-1) + n;
        }
    }



    public static int tinhTongTu1DenNcach3_DeQuy_nhmaChoArray(int[] n, int indexCuoiCungCuaMang){
        if (indexCuoiCungCuaMang == 0){
            return 0;
        } else {
            return tinhTongTu1DenNcach3_DeQuy_nhmaChoArray(n, indexCuoiCungCuaMang-1) + n[indexCuoiCungCuaMang];
        }
    }




    public static int tinhTongCacSoChantu_a_den_b(int a, int b){
        if (a == b){
            return a;
        } else if (a < b) {
            if(b % 2 == 0){
                return tinhTongCacSoChantu_a_den_b(a, b-2) + b;
            } else{
                return tinhTongCacSoChantu_a_den_b(a, b-1) + b;
            }
        }
        return -1;
    }




    public static int tinhTongCacSoChantu_a_den_b_bang_cachBhtg(int a, int b){
        int start = 0;
        int end = 0;
        if ( a % 2 == 0){
            start = a;
        } else {
            start = a + 1;
        }
        if ( b % 2 == 0){
            end = b;
        } else {
            end = b - 1;
        }
        int count = (end-start)/2;

        int sum = (start+end) * count / 2;
        return sum;
    }



    public static int findMaxBangDeQuy(int[] arr, int a, int b){
        if(a == b){
            return arr[a];
        } else{
            int x =  findMaxBangDeQuy(arr, a, b - 1);
            if(x > arr[b]){
                return x;
            } else {
                return arr[b];
            }
        }
    }



    public static boolean searchLinearUsingRercusion(int[] arr, int key, int start, int end){
        if(end==start){ // khi start bang end thi van con 1 phan tu nen phai so sanh no voi key
            return(arr[start] == key);
        } else{
            return searchLinearUsingRercusion(arr, key, start, end-1) || arr[end] == key;
        }
    }



    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }



    public static void reverseUsingRecusrion(int[] arr, int start, int end){
        if(start >= end){
            return;
        } else {
            swap(arr, start, end);
            reverseUsingRecusrion(arr, start + 1, end - 1);
        }
    }


    public static long sumRecur(int start, int end){
        if(end == start){
            return start;
        } else{
            return sumRecur(start, end - 2) + end;
        }


        // c
        //n = end - start
        /* T(n) = T(n-2) + c
                = T(n-4) + 2c
                = T(n-6) + 3c
                ...
                = T(n-n) + n/2 * c

                => O(n)
         */

    }


}
