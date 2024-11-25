class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa
    
    def show_info(self):
        print(self.name)


Kuku = Student('Kuku', 220020, 4.0)
Mici = Student('Mici', 220069, 4.0)
Venuz = Student('Venuz', 220012, 2.5)

list_student = [Kuku, Mici, Venuz]



class Classroom:
    def __init__(self):
        self.students = []
        

    def add(self, s):
        self.students.append(s)

    def remove(self, id):
        for s in self.students:
            if s.id == id:
                self.students.remove(s)

    def find_best(self):
        best = self.students[0]
        for g in self.students:
            if g.gpa > best.gpa:
                g = best
        return best
    

    def find_student(self, name):
        for n in self.students:
            if n.name == name:
                print(n)

#main
muoihaia6 = Classroom()
muoihaia6.add(Student('Be', 105, 3.5))
best = muoihaia6.find_best()
print(muoihaia6.students)
            


        
        
    
        
        

