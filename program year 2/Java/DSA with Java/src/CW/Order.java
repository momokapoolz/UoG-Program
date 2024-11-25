package CW;
import java.util.*;

public class Order {
    private int Id ;
    private String shippingAddress;
    private String books; // List of book titles
    private int quantity;

    //getter
    public int getId(){
        return Id;
    }

    public String getShippingAddress(){
        return shippingAddress;
    }

    public String getBooks(){
        return books;
    }

    public int getQuantity(){
        return quantity;
    }

    //setter
    public void setOrder(int Id, String shippingAddress, String books, int quantity) {
        this.Id = Id;
        this.shippingAddress = shippingAddress;
        this.books = books;
        this.quantity = quantity;
    }
}

