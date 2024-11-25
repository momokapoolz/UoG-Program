package oop;

public class CWflowDemo_product {
    private int id;
    private String name;
    private double price;
    private int quantity;

    //set
    public void setId(int id){
        this.id = id;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setPrice(double price){
        this.price = price;
    }

    public void setQuantity(int quantity){
        this.quantity = quantity;
    }



    //get
    public int getId(){
        return this.id;
    }

    public String getName(){
        return this.name;
    }

    public double getPrice(){
        return this.price;
    }

    public int getIQuantity(){
        return this.quantity;
    }


    /*
    private static ArrayList<product> search (ArrayList<product> products, String input){
        ArrayList<product> found = new ArrayList<product>();

        for (product: products){
            if(product.getName().contains(input)){
                found.add(product);
            }
        }
        return found;
    }
*/
}
