package CW;
import java.util.LinkedList;
import java.util.Queue;

public class OrderQueue {
    private Queue<Order> queue = new LinkedList<>();

    public void enqueue(Order order) {
        queue.offer(order);  // Adds an order to the queue
    }

    public Order dequeue() {
        if (!queue.isEmpty()) {
            return queue.poll();  // Removes and returns the first order
        } else {
            return null;
        }
    }

    public Order peek() {
        if (!queue.isEmpty()) {
            return queue.peek();  // Returns the first order without removing it
        } else {
            return null;
        }
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }
}
