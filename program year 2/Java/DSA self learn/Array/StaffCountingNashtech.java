package Array;
import java.util.*;


class StaffCountingNashtech {

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String input = "SD0123,BPO4567;SD1234,BPO1111;SD222,BPO5678;BPO4568;SD3465\n";

        StaffCounting(input);

//        String str = "mmb, mmmmb, mmb";
//        List<String> elephantList = Arrays.asList(str.split(","));
//        System.out.println("Printing each part:");
//        for (String part : elephantList) {
//            System.out.println(part.trim()); // `trim` removes any leading/trailing spaces
//        }
    }

    private static void StaffCounting(String input) {
        // TODO: Let's Rock 'n Roll here

        int countSD = 0;
        int countBPO = 0;

        List<String> StaffCode = Arrays.asList(input.split(","));

        String eachOneCode = new String();
        System.out.println("Printing each part:");
        for (String e : StaffCode) {
            eachOneCode = e.trim();
            System.out.println(eachOneCode);
        }


        for(int i = 0; i < eachOneCode.length(); i++) {
            if (eachOneCode.charAt(1) == 'S' && eachOneCode.length() == 6) {
                countSD++;
            }
            if (eachOneCode.charAt(1) == 'B' && eachOneCode.length() == 6) {
                countBPO++;
            }
        }

        System.out.println("SD: " + countSD + " BPO: " + countBPO);










//        char[] c = input.toCharArray();
//        int countSD = 0;
//        int countBPO = 0;
//        for (char cha : c){
//            if (cha == 'S'){
//                countSD++;
//            }
//            if(cha == 'B'){
//                countBPO++;
//            }
//        }
//        System.out.println("SD: " + countSD + " BPO: " + countBPO);


    }
}