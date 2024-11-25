package LinkedList;

public class node {
    int data;
    node next;

    //ham khoi tao
    public node(int data){
        this.data = data;
        this.next = null;
    }

    public static void main(String[] args) {
        node one = new node(10);
        node two = new node(100);
        node three = new node(20);
        node four = new node(69);

        //link them to become a linkedlist

        one.next = two;
        two.next = three;
        three.next = four;

        //print
        System.out.println(three.data);
        System.out.println(two.next.next.data);
    }
}
