package Array;
import java.util.Arrays;

public class stockBuyandSell {

    //naive approach
    public static int maxProfit(int[] prices, int start, int end) {
        int res = 0;
        for(int i = start; i < end; i++) {
            for(int j = i+1; j <= end; j++) {
                if (prices[j] > prices[i]) {
                    int current = (prices[j] - prices[i]) + maxProfit(prices, start, i-1) + maxProfit(prices, j + 1, end);
                    res = Math.max(res, current);
                }
            }
        }
        return res;
    }

    public static int maxProfitBetter(int[] prices) {
        int res = 0;
        int lmin = prices[0];
        int lmax = prices[0];
        int i = 0;

        while (i < prices.length-1) {
            //find local minimum
            while (i < prices.length-1 && prices[i] >= prices[i+1]) {
                i++;
            }
            lmin = prices[i];


            //find local maximum
            while (i < prices.length-1 && prices[i] <= prices[i+1]) {
                i++;
            }
            lmax = prices[i];


            res += (lmax - lmin);
        }
        return res;

    }


    public static int maxProfitBest(int[] prices) {
        int res = 0;

        for(int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < prices[i+1]) {
                res = res + prices[i+1] - prices[i];
            }
        }


        return res;
    }



    public static void main(String[] args) {
        int[] prices = {100, 180, 260, 310, 40, 535, 695};
//        int res = maxProfit(prices, 0, prices.length-1);
//        System.out.println(res);

//        int res = maxProfitBetter(prices);
//        System.out.println(res);

        int res = maxProfitBest(prices);
        System.out.println(res);

    }
}
