package CW;
import java.util.*;

public class OrderStack {
    private Stack<Order> stack = new Stack<>();

//    public OrderStack() {
//        stack = new Stack<>();
//    }

    public void push(Order order) {
        stack.push(order);
    }

    public Order pop() {
        if (!stack.isEmpty()) {
            return stack.pop();
        } else {
            return null;
        }
    }

    public Order peek() {
        if (!stack.isEmpty()) {
            return stack.peek();
        } else {
            return null;
        }
    }

    public boolean isEmpty() {
        return stack.isEmpty();
    }
}
