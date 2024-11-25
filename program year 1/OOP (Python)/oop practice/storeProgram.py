#STORE
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
        for i in self.product:
            if i.stock == 0:
                return i
            

#STORE PROGRAM 
class StoreProgram:
    def __init__(self):
        self.store = Store
    
    def print_menu(self):
        for i in self.store:
            print(i)
            print("1. Add production"
                  "2. Remove product"
                  "3. Show all product"
                  "4. Find product by name"
                  "5. Find empty stocks")
            
    def get_option(self):
        i = int(input("Please enter an option: "))
        if i in range(1, 6):
            if i == 1:
                return 'Add'
            if i == 2:
                return 'Remove'
            if i == 3:
                return 'Show all'
            if i == 4:
                return 'Find product'
            if i == 5:
                return 'Find Stock'
        else:
            return 'Invalid option'
        
    def do_task(self, option):
        option = self.get_option()
        if option == 'Add':
            self.store.add()
        if option == 'Remove':
            self.store.remove()
        if option == 'Show all':
            self.store.show_all()
        if option == 'Find product':
            self.store.find_name()
        if option == 'Finf stock':
            self.store.find_empty()
    
    def run(self):
        while True:
            self.print_menu()
            self.get_option()
            self.do_task()

            
            
        

            


