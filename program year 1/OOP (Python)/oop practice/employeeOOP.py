class Employee:
    def __init__(self, name, rate):
        self.__name = name
        self.__rate = rate
        self._salary = 1000

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError('No name bri')
        self.__name = value

    @property
    def rate(self):
        return self.__rate
    
    @rate.setter
    def rate(self, value):
        if len(value) <= 0:
            raise ValueError('No rate bri')
        self.__rate = value


    def salary(self):
        return self.rate * self._salary  #truy cap den ham getter ae
    

    def show_info(self):
        print(self.__name)
        print()
        print(self.__rate)
        print()
        print(self.salary())



class PartTimeEmployee(Employee):
    def __init__(self, name, rate, days):
        super().__init__(name, rate)
        self.__days = days

    def salary(self):
        return super().salary() * self.__days / 5
    
    def show_info(self):
        return super().show_info()
    



class Company:
    def __init__(self, name):
        self.__name = name
        self.__full_times = []
        self.__part_times = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name
    
    def add_full(self, emp):
        # check if emp is an instance of Employee
        if not isinstance(emp, Employee):
            raise ValueError("Must be an instance of Employee")
        
        self.__full_times.append(emp)

    def add_part(self, emp):
        if not isinstance(emp, PartTimeEmployee):
            raise ValueError("Must be an instance of PartTimeEmployee")
        
        self.__part_times.append(emp)
    
    def show_employees(self):
        print('Full time employees:')
        for e in self.__full_times:
            e.show_info()
        print('Part time employees:')
        for e in self.__part_times:
            e.show_info()
    



#MAIN AE
def input_fulltime():
    name = input('what your name ae: ')
    rate = float(input('how much rate ae: '))
    return Employee(name, rate)

def input_parttime():
    name = input('what your name ae: ')
    rate = float(input('how much rate ae: '))
    days = int(input('how many days ae: '))
    return PartTimeEmployee(name, rate, days)


def manage_employee():
    fulltime = []
    parttime = []
    fulltime.append(input_fulltime())
    parttime.append(input_parttime())
    A = Company(fulltime, parttime)
    return A


def program():
    running = True
    while running:
        print('1. add full time employee')
        print('2. add part time employee')
        print('3. show all employees')
        print('4. quit')
        choice = int(input("Enter choice: "))







    


    

    