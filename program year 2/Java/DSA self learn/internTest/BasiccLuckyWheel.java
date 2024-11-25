package internTest;

import java.util.*;


//ddeef baif
//Chức năng vòng quay may mắn có thể tặng cho khách hàng 8 phần thưởng khác nhau với tỉ lệ trúng thưởng như sau:
//Phần thưởng 01 tỉ lệ trúng 1%
//Phần thưởng 02 tỉ lệ trúng 4%
//Phần thưởng 03 tỉ lệ trúng 10%
//Phần thưởng 04 tỉ lệ trúng 15%
//Phần thưởng 05 tỉ lệ trúng 15%
//Phần thưởng 06 tỉ lệ trúng 15%
//Phần thưởng 07 tỉ lệ trúng 15%
//Phần thưởng 08 tỉ lệ trúng 25%
//Tuy nhiên phần thường 01 và 02 có giá trị cao nên cần đảm bảo không cho phép trao thưởng với tỉ lệ sai số quá 2%.



public class BasiccLuckyWheel {
    Random random;

    public int[] suffleReward;  //1 mang chua cac phan thuong sap xep ngau nhien

    private int[] prizeCount;   //ddem so cac lan thang cua tung giai thuong

    private int spinCount;   //dem sso lan quay

    int[] percentages;

    double[] allowable_deviation;  //sai so hop le

    int errorCount;


    public BasiccLuckyWheel(int[] percentages, double[] allowable_deviation){  //constructor
        List<Integer> suffleList = new LinkedList<>();

        for(int i = 0; i < percentages.length; i++){
            for(int j = 0; j < percentages[i]; j++){
                suffleList.add(i);
            }
        }
//        //Một vòng lặp lặp qua mảng tỷ lệ phần trăm, trong đó mỗi chỉ số đại diện cho một giải thưởng cụ thể và giá trị tại mỗi chỉ số thể hiện xác suất chiến thắng của nó.
//        Đối với mỗi giải thưởng, một vòng lặp bên trong lặp lại số lần được chỉ định theo tỷ lệ phần trăm[i]. Trong mỗi lần lặp, nó thêm chỉ số giải thưởng i vào suffleList.
//        Cách tiếp cận này chuẩn bị một cách hiệu quả một danh sách trong đó mỗi giải thưởng xuất hiện tương ứng với xác suất của nó.

        Collections.shuffle(suffleList);

        this.suffleReward = suffleList.stream().mapToInt(Integer::intValue).toArray();
        this.prizeCount = new int[percentages.length];
        this.spinCount = 0;
        this.random = new Random();
        this.percentages = percentages;
        this.allowable_deviation = allowable_deviation;
    }

    public int spin(){
        do{
            int random_index = random.nextInt(suffleReward.length);
            int prize_index = suffleReward[random_index];
            if (prize_index < allowable_deviation.length){ // Ensures that the prize_index is within bounds for allowable_deviation
                int rewardCount = prizeCount[prize_index] + 1; //The potential new count of the selected prize if this spin succeeds.
                int newSpinCount = spinCount + 1;
                double deviation = (1.0 * rewardCount / newSpinCount) - (1.0 * percentages[prize_index] / 100);

                //Tính toán độ lệch giữa tần suất trúng thưởng của giải thưởng so với xác suất mục tiêu của nó. Điều này so sánh tỷ
                // lệ của rewardCount với newSpinCount so với tỷ lệ phần trăm dự kiến cho giải thưởng.

                if(deviation >= allowable_deviation[prize_index]){ //checks if the calculated deviation is beyond the allowable range for this prize.
                    errorCount++;
                    continue;
                }
            }

            prizeCount[prize_index]++;
            spinCount++;
            return prize_index;

        }while(true);
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append("basic lucky wheel: ");
        sb.append("\nSpin Count: ");
        sb.append("\nPrize Count: ");
        sb.append("\nError Count: ");
        sb.append("\n");
        return sb.toString();
    }

    public String intArrayToString(int[] rewardCount){
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for(int i = 0; i < rewardCount.length; i++){
            if (i < rewardCount.length - 1){
                sb.append(rewardCount[i]).append(",");
            } else {
                sb.append(rewardCount[i]);
            }
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args){
        int[] percentages = {1, 4, 10, 15, 15, 15, 25};
        double[] allowable_deviation = new double[]{0.02, 0.02};
        BasiccLuckyWheel basicLuckyWheel = new BasiccLuckyWheel(percentages, allowable_deviation);
        int totalSpin = 1000000;
        int[] prizeCounts = new int[basicLuckyWheel.suffleReward.length];
        int spinCount = 0;
        for(int i = 0; i < totalSpin; i++) {
            int prize = basicLuckyWheel.spin();
            spinCount++;
            prizeCounts[prize]++;
            if(prize < allowable_deviation.length){
                double deviation = (1.0 * prizeCounts[prize] / spinCount) - (1.0 * percentages[prize] / 100);
                if(deviation >= allowable_deviation[prize]){
                    throw new RuntimeException("deviation rejected");
                }
            }
        }
        System.out.println(basicLuckyWheel);
    }

}



