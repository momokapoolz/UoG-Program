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

class Store:
    def __init__(self):
        self.product = []

    def add(self, p):
        self.product.append(p)

    def remove(self, name):
        for p in self.product:
            if p.name == name:
                self.product.remove(p)

    def show_all(self):
        for p in self.product:
            print(p)

    def find_name(self, name):
        for p in self.product:
            if p.name == name:
                print(p)
    
    def find_empty(self):
        for i in Product:
            if i.stock == 0:
                return i

        
