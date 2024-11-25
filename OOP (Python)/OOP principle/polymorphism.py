import math
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name):
        self._name = name

    
    @property
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self._name} - area: {self.area}'

#hinh tron
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self.radius ** 2
    
    def __str__(self):
        return super().__str__() + f', radius: {self.radius}'
    
#hinh chu nhat
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value


    @property
    def height(self): #xong ham getter lai goi ve attribute (doc tu duoi ae)
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self.height * self.width #goi ve ham getter 
    

    def __str__(self):
        return super().__str__() + f', height: {self.height}, width: {self.width}'
    
#hinh tam giac
class Triangle(Shape):
    def __init__(self, name, sideA, sideB, sideC):
        super().__init__(name)
        self._sideA = sideA
        self._sideB = sideB
        self._sideC = sideC

    @property
    def sideA(self):
        return self._sideA
    
    @sideA.setter
    def sideA(self, value):
        if value <= 0:
            raise ValueError("sideA must be positive")
        if self.check_sum(value, self.sideB, self.sideC):
            raise ValueError("me may beo")
        self._sideA = value


    @property
    def sideB(self): #xong ham getter lai goi ve attribute (doc tu duoi ae)
        return self._sideB
    
    @sideB.setter
    def sideB(self, value):
        if value <= 0:
            raise ValueError("sideB must be positive")
        if self.check_sum(self.sideA, value, self.sideC):
            raise ValueError("me may beo")
        self._sideB = value


    @property
    def sideC(self): #xong ham getter lai goi ve attribute (doc tu duoi ae)
        return self._sideC
    
    @sideC.setter
    def sideC(self, value):
        if value <= 0:
            raise ValueError("sideC must be positive")
        if self.check_sum(self.sideA, self.sideB, value):
            raise ValueError("me may beo")
        self._sideC = value

    def check_sum(a, b, c):
        return a+b > c and b+c > a and c+a > b


    @property
    def area(self):
        p = (self.sideA + self.sideB + self.sideC) / 2
        return math.sqrt(p*(p - self.sideA)*(p - self.sideB)*(p - self.sideC))
    

    def __str__(self):
        return super().__str__() + f', sideA: {self.sideA}, sideB: {self.sideB}, sideC: {self.sideC}'
    


#tam giac can
class IsoTriangle(Triangle):
    def __init__(self, name, side, base):
        super().__init__(name, side, side, base)
    
    @property
    def side(self):
        return self.sidea # or sideb

    @side.setter
    def side(self, value):
        self.sidea = value # call setter of parent class, already validated
        self.sideb = value
    
    @property
    def base(self):
        return self.sidec
    
    @base.setter
    def base(self, value):
        self.sidec = value

    
    def __str__(self):
        return super().__str__() + f'side: {self.side}, base: {self.base}'



#MAIN AE
#obj1 = Shape('kobiet')
obj2 = Circle('Maru', 13)
obj3 = Rectangle('Be', 64, 26)
obj4 = Triangle('iluminati', 3, 4, 5)
obj5 = IsoTriangle('me may', 4, 6)

shapes = [obj2, obj3, obj4, obj5]
for s in shapes:
    print(s.area)