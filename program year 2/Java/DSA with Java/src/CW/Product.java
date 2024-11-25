package CW;

public class Product {
    private String name;
    private float price;
    private int quantity;

    //name getter
    public String getName(){
        return name;
    }

    //price getter
    public float getPrice(){
        return price;
    }

    //quantity getter
    public int getQuantity(){
        return quantity;
    }


    //setter
    public void setAll(String newName, float newPrice, int newQuantity){
        this.name = newName;
        this.price = newPrice;
        this.quantity = newQuantity;
    }




}
