def list_pizza():
    pizza_types = ["margherita", "napoletana", "marinara"]
    pizza_prices = [6.0, 7.0, 7.5]
    extra_types = ["mushrooms", "cheese", "anchovies", "sausage"]
    extra_prices = [0.5, 1.0, 1.5, 1.8]
    print(pizza_types, pizza_prices, extra_types, extra_prices)
    return pizza_types, pizza_prices, extra_types, extra_prices

    
def price_pizza_calculate(order):
    total_price = 0
    if(order == "margherita"):
        total_price += 6.0
    if(order == "napoletana"):
        total_price += 7.0
    if(order == "marinara"):
        total_price += 7.5
    return total_price


def price_topping_calculate(order2):
    total_price = 0
    if(order2 == "mushroom"):
        total_price += 0.5
    if(order2 == "cheese"):
        total_price += 1.0
    if(order2 == "anchovies"):
        total_price += 1.5
    if(order2 == "marinara"):
        total_price += 1.8
    return total_price




    
def take_order():
    total_price = 0
    order = input("ban muon an pizza gi: ")
    order_line = price_pizza_calculate(order)
    order_amount = int(input("ban muon lay bao nhieu cai: "))
    total_price = order_line * order_amount
    
    order2 = input("ban muon an toping gi: ")
    order2_line = price_topping_calculate(order2)
    total_price_sum = total_price + order2_line

    print("cua ban la:", total_price_sum)

#main function
list_pizza()
take_order()



            
     









