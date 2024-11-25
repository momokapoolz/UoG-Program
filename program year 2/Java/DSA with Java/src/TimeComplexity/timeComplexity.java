package TimeComplexity;

public class timeComplexity {
    public static void main(String[] args) {
        int n = 2;


        for (int i = 1; i <= n; i++){			//Outer loop
            for(int j = 1; j <= n; j = j * 2) {	//Inner loop
                System.out.println("Hey - I'm busy looking at: " + i + " and " + j);
            }
        }


        int mat[][] = {};


        //6.1
        for (int i = 0; i < n; i++) //n step
            for (int j = 0; j < n; j++) // n step in each step in n => n*n
                mat[i][j] = 0;
        for (int k = 0; k < n; k++)// n step
            mat[k][k] = 1;

        //n*n+n = n^2 + n = n^2


        int A[][] = {};
        //6.2
        for(int i = 0; i< n ; i ++){ //n step
            for(int j = 0; j < n; j ++){ //n step in each step in n => n*n
                A[i][j] = 0 ;
            }
            for(int k = 0;  k < n; k++){ //n step in each step in n => n*n
                A[k][k] = 1;
            }
        }

        //n(n+n) = n(2n) = 2n^2 = n^2




        for(int i = 0; i < n;  i++){ //n step
            for(int j = 0; j < n; j++){ //n step in each step in n => n*n
                A[i][j] = 0;
                for(int k = 0;  k < n; k++){ //n step in each step in n => n*n
                    A[k][k] = 1;
                }
            }
        }

    }
}
