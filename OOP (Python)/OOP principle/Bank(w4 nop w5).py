#ACCOUNT
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
            print("Not enough")
        if amount <= 0:
            print("you can not withddraw 0")
        else:
            self.__balance -= amount
            print("Account balance now: ",self.__balance,"-",amount)


    #deposit: nap tien
    def deposit(self, amount):
        if amount <= 0:
            print("you can not deposit 0")
        else:
            self.__balance += amount
            print("Account balance now: ",self.__balance,"-",amount)


    #transfer: chuyen tien
    def transfer(self, amount, other_account):
        if amount > self.__balance:
            print("Not enough")
        if amount <= 0:
            print("you can not withddraw 0")
        else:
            self.balance -= amount
            other_account.balance += amount
            print("Transfered",amount,"to this account")


    def show(self):
        print("name:",self.__name)
        print()
        print("balance:",self.__balance)
        print()
        print("id:",self.__id)



#BANK 
class Bank:
    def  __init__(self, name=''):
        self.__account = []
        self.__name = name

    def add(self, a):
        self.__account.append(a)

    #get id tim acc
    def __get_id(self, id):
        for acc in self.__account:
            if acc.id == id:
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

    #chuyen tien
    def transfer(self, source_id, dest_id, amount):
        acc = self.__get_id(source_id)
        another_acc = self.__get_id(dest_id)
        if acc == None or another_acc == None:
            print("wtf bro")
        else:
            acc.transfer(amount, another_acc)

    
    def show(self, id):
        acc = self.__get_id(id)
        for acc in self.__account:
            if acc.id == id:
                print(acc.account)
                print()
                print(acc.name)

#BANK PROGRAM
class BankProgram:
    def __init__(self):
        self.__bank = []

    def print_menu():
        print("1. add account")
        print("2. show all")
        print("3. get account id")
        print("4. show account")
        print("5. withdraw")
        print("6. deposit")
        print("7. transfer")
    
    def get_option(self, option):
        option = int(input("enter option: "))
        return option
    
    def do_task(self, option):
        if option == 1:
            Bank.add()
            print("added;")
        elif option == 2:
            for c in len(self.__bank):
                print(self.__bank[c])
        elif option == 3:
            Bank.__get_id()
        elif option == 4:
            Bank.show()
        elif option == 5:
            Bank.withdraw()
        elif option == 6:
            Bank.deposit()
        elif option == 7:
            Bank.transfer()








        








    





    
