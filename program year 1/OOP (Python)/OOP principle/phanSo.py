class Fraction:
    def __init__(self, tuso = 0, mauso = 1):
        self.__tuso = tuso
        self.__mauso = mauso

    def get_tuso(self):
        return self.__tuso
    
    def set_num(self, tuso):
        self.__tuso = tuso

    def get_mauso(self):
        return self.__mauso
    
    def set_mauso(self, mauso):
        if mauso > 0:
            self.__mauso = mauso
        else:  
            print("break")

    def show(self):
        print(self.__tuso,"/",self.__mauso, end='')
    
    def add(self, f):
        n = self.__tuso * f.get_mauso() + self.__mauso * f.get_tuso()
        d = self.__mauso * f.get_mauso()
        return Fraction(n, d)
    
    def minus(self, f):
        n = self.__tuso * f.get_mauso() - self.__mauso * f.get_tuso()
        d = self.__mauso * f.get_mauso()
        return Fraction(n, d)
    
    def mul(self, f):
        n = self.__tuso * f.get_tuso()
        d = self.__mauso * f.get_mauso()
        return Fraction(n, d)
    
    def division(self, f):
        if f.get_tuso() == 0:
            print("no")
            return None
        n = self.__tuso * f.get_mauso()
        d = self.__mauso * f.get_tuso()
        return Fraction(n, d)

#demo
def demoPhanso():
    running = True
    while(running):
        tuso1 = int(input("Nhap tu so 1: "))
        mauso1 = int(input("Nhap mau so 1: "))
        ps1 = Fraction(tuso1, mauso1)

        tuso2 = int(input("Nhap tu so 2: "))
        mauso2 = int(input("Nhap mau so 2: "))
        ps2 = Fraction(tuso2, mauso2)

        print("Chon 1 phep tinh: "
              "1) Cong "
              "2) Tru "
              "3) Nhan "
              "4) Chia "
              "5) Break ")

        option = int(input("Enter your option: "))
        if(option == 1):
            f1 = ps1.add(ps2)
            f1.show()
            print()
        if(option == 2):
            f2 = ps1.division(ps2)
            f2.show()
            print()
        if(option == 3):
            f3 = ps1.mul(ps2)
            f3.show()
            print()
        if(option == 4):
            f4 = ps1.division(ps2)
            f4.show()
            print()
        if(option == 5):
            running = False

#main ae
demoPhanso()





