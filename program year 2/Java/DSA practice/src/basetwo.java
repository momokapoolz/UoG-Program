import java.util.Scanner;

public class basetwo {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        String n = basetwoconvert(a);

        System.out.print(n);
    }

    public static String basetwoconvert(int a){
        String bina = "";
        while(a > 0){
            int remainder = a % 2;
            bina = remainder + bina;
            a = a / 2;
        }
        return bina;
    }


}
