package Recursion;

public class fibonacciRecursion {
    public static void main(String[] args) {

    }

    public int fib(int n){
        if(n <= 2){
            return 1;
        } else {
            return fib(n-1) + fib(n-2);
        }

        //
    }

    //memorize technique: ki thuat ghi nho cac phep tinh da tinh r de ko phai tinh lai
    public static long fibAdv(int n, long[] mem){
        if(n <= 2){
            mem[n] = 1;
        } else {
            if(mem[n] == 0){
                mem[n] = fibAdv(n-1, mem) + fibAdv(n-2, mem);
            }
        }

        return mem[n];
    }
}
