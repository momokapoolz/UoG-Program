class Vtuber:
    def __init__(self, name = '', id = 0, company = ''):
        self.name = name ##public
        self.__id = id #private
        self.company = company #public

    def show_info(self):
        print("Vtuber name: ", self.name)
        print("Vtuber ID: ", self.__id)
        print("Vtuber company: ", self.company)
    
    def set_id(self, id):
        if id >= 0:
            self.__id = id
        else:
            print("Invalid")


Watame = Vtuber('Tsunomaki Watame', 606 , 'Hololive')

Watame.__id = 69 # no because cannot access outside 
print(Watame.__id)
Watame.set_id(69) # ok because we call public function inside instead from outside
print(Watame.set_id())
