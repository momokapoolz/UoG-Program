package LinkedList;


class advanceNode<T> {
    private T data;

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public advanceNode<T> getPrev() {
        return prev;
    }

    public void setPrev(advanceNode<T> prev) {
        this.prev = prev;
    }

    public advanceNode<T> getNext() {
        return next;
    }

    public void setNext(advanceNode<T> next) {
        this.next = next;
    }

    private advanceNode<T> prev, next;

    public advanceNode(T data, advanceNode<T> prev, advanceNode<T> next) {
        this.data = data;
        this.prev = prev;
        this.next = next;
    }

    @Override
    public String toString() {
        return data.toString();
    }
}
