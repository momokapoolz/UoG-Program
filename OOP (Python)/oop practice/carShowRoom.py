class Car:
    def __init__(self):
        self.model = ''
        self.price = 0
        self.brand = ''
        self.speed = 0
    def show_info(self):
        print(self.model)
        print()
        print(self.price)
        print()
        print(self.brand)
        print()
        print(self.speed)
        print()

Mercesdes = Car('Mec', 300000000, 'Mec', 200)
Lamboghini = Car('Lambo', 123456000000, 'Lambo', 500)

class ShowRoom:
    def __init__(self):
        self.car = Car
        self.name = ''
        self.income = 0
    def showroom(self):
        for c in self.car:
            print(c)

    def sell(self):
        c = input('Car model: ')
        for i in self.car:
            if self.car[i] == c:
                self.income += 0
        print('error')

class ShowRoomProgram:
    def __init__(self):
        self.showroom = ShowRoom
    def print_menu():
        print("1. Show all cars.\
               2. Add new Car.\
               3. Sell a Car.\
               4. Show showroom income.")
    def get_option(self, c):
        option = 0
        cars = Car
        input(int('Please enter a number only included in the menu has shown.'))
        if option == 1:
            print(Car)
        elif option == 2:
            for c in cars:
                ShowRoom.add_car()
                print("Car {c.name} has been added")
            else:
                return
        elif option == 3:
            ShowRoom.sell_car()
        elif option == 4:
            print()    

