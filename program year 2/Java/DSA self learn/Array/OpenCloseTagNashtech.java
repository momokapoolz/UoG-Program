package Array;

import java.util.*;

class OpenCloseTagNashtech {
    private static boolean IsValid(char[] input) {

        Stack<Character> stack = new Stack<>();


        Map<Character, Character> tagPairs = Map.of(
                ')', '(',
                '}', '{',
                ']', '[',
                '>', '<'
        );


        for (char c : input) {
            if (tagPairs.containsValue(c)) {

                stack.push(c);
            } else if (tagPairs.containsKey(c)) {

                if (stack.isEmpty() || stack.pop() != tagPairs.get(c)) {
                    return false;
                }
            }
        }


        return stack.isEmpty();
    }

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int cases = Integer.parseInt(scanner.nextLine());

        for (int i = 1; i <= cases; ++i) {
            char[] line = scanner.nextLine().toCharArray();
            if (IsValid(line)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}