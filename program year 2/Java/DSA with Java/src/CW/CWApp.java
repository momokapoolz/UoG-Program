package CW;
import java.util.ArrayList;
import java.util.Scanner;


public class CWApp {

    //define order stack here
    public static OrderStack orderStack = new OrderStack();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;

        //Initialize products

        Product p1 = new Product();
        p1.setAll("Summer Tunnel", 1200, 20);

        Product p2 = new Product();
        p2.setAll("3 days of happiness", 1500, 20);

        Product p3 = new Product();
        p3.setAll("Oregairu", 1800, 20);

        Product p4 = new Product();
        p4.setAll("Bunny Girl Senpai", 1100, 20);

        Product p5 = new Product();
        p5.setAll("Rezero", 1000, 20);

        ArrayList<Product> products = new ArrayList<Product>();
        products.add(p1);
        products.add(p2);
        products.add(p3);
        products.add(p4);
        products.add(p5);


        //order stack
        //OrderStack orderStack = new OrderStack();


        do{
            //clear the console screen
            System.out.print("\033[H\033[2J");
            System.out.println("Welcome to the online store");
            System.out.println("1. Product List");
            System.out.println("2. Make orders");
            System.out.println("3. Search Product");
            System.out.println("4. Sort all products by price");
            System.out.println("5. Sort all products by name");
            System.out.println("6. My orders");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");
            choice = sc.nextInt();
            switch(choice){
                case 1:
                    printProducts(products);
                    break;
                case 2:
                    makeOrder(products);
                    break;
                case 3:
                    Scanner sca = new Scanner(System.in);
                    //sca.nextLine();

                    System.out.println("Enter product's name:");
                    String searchInput = sca.nextLine();

                    Product searchProductName = searchProductByName(products, searchInput);
                    System.out.println(searchProductName.getName() + ";" + searchProductName.getPrice());
                    break;
                case 4:
                    ArrayList<Product> ssortByPrice = sortByPrice(products);
                    for (Product product : ssortByPrice) {;
                        System.out.println(product.getName() + ";" + product.getPrice());
                    }
                    break;
                case 5:
                    ArrayList<Product> ssortByName = sortByName(products);
                    for (Product product : ssortByName) {;
                        System.out.println(product.getName() + ";" + product.getPrice());
                    }
                    break;
                case 6:
                    viewOrder(orderStack);
                    break;
                default:

            }
        }while(choice != 7);
    }



    //1.List all product
    private static void printProducts(ArrayList<Product> products) {
        for (Product product : products) {;
            System.out.println(product.getName() + ";" + product.getPrice());
        }
    }


    //2.make order
    private static void makeOrder(ArrayList<Product> products){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter product id:");
        int choice = sc.nextInt();

        sc.nextLine();

        System.out.println("Enter shipping address:");
        String shippingAddress = sc.nextLine();


        System.out.println("Enter quantity:");
        int quantity = sc.nextInt();



        if(choice < 0 || choice > products.size()){
            System.out.println("Product does not exist");
        } else{
            switch (choice){
                case 1:
                    Order o1 = new Order();
                    o1.setOrder(1, shippingAddress, "Summer Tunnel", quantity );
                    orderStack.push(o1);
                    break;
                case 2:
                    Order o2 = new Order();
                    o2.setOrder(1, shippingAddress, "3 days of happiness", quantity );
                    orderStack.push(o2);
                    break;
                case 3:
                    Order o3 = new Order();
                    o3.setOrder(1, shippingAddress, "Oregairu", quantity );
                    orderStack.push(o3);
                    break;
                case 4:
                    Order o4 = new Order();
                    o4.setOrder(1, shippingAddress, "Bunny Girl Senpai", quantity );
                    orderStack.push(o4);
                    break;
                case 5:
                    Order o5 = new Order();
                    o5.setOrder(1, shippingAddress, "Rezero", quantity );
                    orderStack.push(o5);
                    break;
            }
        }
    }

    //3.search product
    private static Product searchProductByName(ArrayList<Product> products, String sth){
        for(Product product : products){
            if(product.getName().equalsIgnoreCase(sth)){
                return product;
            }
        }
        return null;
    }






    //4 sort by price
    private static ArrayList<Product> sortByPrice(ArrayList<Product> products){
        ArrayList<Product> newProductsList = new ArrayList<>(products);


        for(int i = 0; i < newProductsList.size(); i++){
            boolean swapped = false;
            for(int j = 0; j < newProductsList.size()-i-1; j++){

                if(newProductsList.get(j).getPrice() > newProductsList.get(j+1).getPrice()){
                    Product temp = newProductsList.get(j);
                    newProductsList.set(j, newProductsList.get(j + 1));
                    newProductsList.set(j + 1, temp);
                    swapped = true;
//                    int temp = arr[j];
//                    arr[j] = arr[j+1];
//                    arr[j+1] = temp;
//                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return newProductsList;
    }










   //5 sort by name
    private static ArrayList<Product> sortByName(ArrayList<Product> products){
        ArrayList<Product> newProductsList = new ArrayList<>(products);


        for(int i = 0; i < newProductsList.size(); i++){
            boolean swapped = false;
            for(int j = 0; j < newProductsList.size()-i-1; j++){
                if(newProductsList.get(j).getName().compareToIgnoreCase(newProductsList.get(j+1).getName()) > 0){
                    Product temp = newProductsList.get(j);
                    newProductsList.set(j, newProductsList.get(j + 1));
                    newProductsList.set(j + 1, temp);
                    swapped = true;
//                    int temp = arr[j];
//                    arr[j] = arr[j+1];
//                    arr[j+1] = temp;
//                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return newProductsList;
    }


    //6 see order
    private static void viewOrder(OrderStack orderStack){

        System.out.println(orderStack);


    }




}
