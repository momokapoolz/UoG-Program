#PARENT CLASS
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(self.__name, self.__age)


#CHILD CLASS
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.__gpa = gpa

    def show(self):
        super().show()
        print(self.__gpa)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def show(self):
        super().show()
        print(self.__subject)


me = Person('Be', 19)
me.show()

you = Student('oOo', 19, 4.0)
you.show()

her = Teacher('Kafka', 32, 'Math')
her.show()