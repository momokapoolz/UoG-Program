class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
    
    @property
    def numerator(self):
        return self.__numerator
    
    @property
    def denominator(self):
        return self.__denominator
    
    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"
        
    def add(self, f):
        n = self.numerator * f.denominator + self.denominator * f.numerator
        d = self.denominator * f.denominator
        return Fraction(n, d)
    

    



