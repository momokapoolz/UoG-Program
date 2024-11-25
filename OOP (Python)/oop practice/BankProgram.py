import random

#Account ni oi
class Account:
    def __init__(self, name='', balance = 0.0, id = 0, MAX_amount = 0):
        self.__name = name
        self.__balance = balance
        self.__id = id
        self.__MAX_amount = MAX_amount

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            print("Invalid")
        else:
            self.__name = name
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("Invalid")
        else:
            self.__balance = balance 

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id


    #withdraw : rut tien
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough")
        if amount <= 0:
            raise ValueError("you can not withddraw 0")
        if amount > self.__MAX_amount:
            raise ValueError("Too much")
        else:
            self.__balance -= amount
            print("Account balance now: ",self.__balance,"-",amount)


    #deposit: nap tien
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("you can not deposit 0")
        else:
            self.__balance += amount
            print("Account balance now: ",self.__balance,"-",amount)

#Ham con
class debitAccount(Account):
    def __init__(self, name='', balance=0, id=0, MAX_amount=0, limit=0):
        super().__init__(name, balance, id, MAX_amount)
        self.limit = limit

class normalAccount(Account):
    def __init__(self, name='', balance=0, id=0, MAX_amount=0, fee = 1):
        super().__init__(name, balance, id, MAX_amount)
        self.fee = fee

class VIPAccount(Account):
    def __init__(self, name='', balance=0, id=0, MAX_amount=0):
        super().__init__(name, balance, id, MAX_amount)

#menu program
class MenuProgram:
    def __init__(self):
        self.normal_account = []
        self.debit_account = []
        self.vip_account = []


    def run(self):
        self.running = True
        while self.running:
            self.print_menu()
            self.do_task(self, self.get_option(self))
            if self.get_option() == 7:
                self.running = False
                break

    def print_menu():
        print("1. add normal account")
        print("2. add vip account")
        print("3. add debit account")
        print("4. search")
        print("5. withdraw")
        print("6. deposit")
        print("7. quit")
        
    
    def get_option(self):
        option = int(input("Enter option: "))
        return option
    

    def do_task(self, option):
        if option == 1:
            a = normal_account_config()
            BankProgram.add_normal_account(self, a)
            print("added normal account")
        elif option == 2:
            a = vip_account_config()
            BankProgram.add_vip_account(self, a)
            print("added VIP account")
        elif option == 3:
            a = debit_account_config()
            BankProgram.add_debit_account(self, a)
            print("added debit account")
        elif option == 4:
            result = BankProgram.search()
            if result == None:
                print("Not found")
            else:
                print("Founded", result)
        elif option == 5:
            BankProgram.withdraw()
        elif option == 6:
            BankProgram.deposit()



#Bank program
class BankProgram(MenuProgram):
    def __init__(self):
        super().__init__()
        
    #3 ham add account ae
    def add_normal_account(self, a):
        self.normal_account.append(a)

    def add_vip_account(self, a):
        self.vip_account.append(a)

    def add_debit_account(self, a):
        self.debit_account.append(a)


    #search ae
    def search(self, id):
        for acc in self.normal_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        for acc in self.vip_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        for acc in self.debit_account:
            if acc.id == id:
                print("Found", acc)
                return acc
        return None

    #rut tien
    def withdraw(self, id, amount):
        acc = self.__get_id(id)
        if acc == None:
            print("wtf bro")
        else:
            acc.withdraw(amount)
    
    #nap tien
    def deposit(self, id, amount):
        acc = self.__get_id(id)
        if acc == None:
            print("wtf bro")
        else:
            acc.deposit(amount)

#main(chac the)
def random_number():
    a = []
    for i in range(1, 6):
        a.append(random.randint(0, 9))
    return a

#account config(cha biet dung ko)
def normal_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = normalAccount(name, balance, id, MAX_amount)
    return a

def vip_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = VIPAccount(name, balance, id, MAX_amount)
    return a

def debit_account_config():
    name = input("Enter name account: ")
    id = random_number()
    balance = 0
    MAX_amount = 0
    a = debitAccount(name, balance, id, MAX_amount)
    return a

#DAY MOI LA MAIN AE
menuprogram = MenuProgram
menuprogram.run(menuprogram)





