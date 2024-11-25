package Stack;

import CW.Order;

public class Stack {
    private java.util.Stack<Order> stack = new java.util.Stack<>();



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
