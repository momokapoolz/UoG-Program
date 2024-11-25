class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def show_info(self):
        print(self.name)
        

    def show_stock(self):
        print(self.price)
        print(self.stock)



#main
akko = Product('chat cam', '10000$', 69)
ktt = Product('ktt', '2000$', 6.9)
omae_no_okaasan = Product('omae_no_okaasan', '69000$', 690)

list_pro = [akko, ktt, omae_no_okaasan]
for i in list_pro:
    print(i.show_info())
    print(i.show_stock())
