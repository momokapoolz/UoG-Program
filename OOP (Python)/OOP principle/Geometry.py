from polymorphism import Shape, Circle, Rectangle, Triangle, IsoTriangle
from abc import ABC, abstractmethod


class Menu(ABC):
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = self.get_option()
            self.do_task(choice)

            if choice == 0:
                running = False

    @abstractmethod
    def print_menu(self):
        pass

    def get_option(self):
        choice = int(input('Enter your choice: '))
        return choice
    
    @abstractmethod
    def do_task(self, choice):
        pass


class DemoShape(Menu):
    def __init__(self):
        super().__init__()
        self.shape = []


    def print_menu(self):
        print("1. Add a circle")
        print("2. Add a rectangle")
        print("3. Add a triangle")
        print("4. Add an isosceles triangle")
        print("5. Display all shapes")
        print("0. Quit")


    def add_circle(self):
        a = input("Circle name? ")
        r = float(input("add radius? "))
        try:
            new_circle = Circle(a, r)
            self.shape.append(new_circle)
        except ValueError as e:
            print(e, 'ko dc ae')
    
    def add_rectangle(self):
        a = input("Rectangle name? ")
        b = float(input("add height? "))
        c = float(input("add width? "))
        new_rectangle = Rectangle(a, b, c)
        self.shape.append(new_rectangle)

    def add_triangle(self):
        a = input("Triangle name? ")
        b = float(input("add sideA? "))
        c = float(input("add sideB? "))
        d = float(input("add sideC? "))
        new_triangle = Triangle(a, b, c, d)
        self.shape.append(new_triangle)

    def add_iso_triangle(self):
        a = input("IsoTriangle name? ")
        s = float(input("add side? "))
        b = float(input("add base? "))
        new_IsoTriangle = IsoTriangle(a, s, b)
        self.shape.append(new_IsoTriangle)

    def get_option(self):
        choice = int(input('Enter your choice: '))
        return choice
    
    def do_task(self, choice):
        if choice == 1:
            self.add_circle()
        if choice == 2:
            self.add_rectangle()
        if choice == 3:
            self.add_triangle()
        if choice == 4:
            self.add_iso_triangle()
        if choice == 5:
            for i in range (len(self.shape)):
                print(self.shape[i])

    def run(self):
        return super().run()


