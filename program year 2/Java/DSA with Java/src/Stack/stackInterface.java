package Stack;

public interface stackInterface<T> extends Iterable<T> {
    void push(T element);
    T pop();
    T top();
}
