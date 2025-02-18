class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(str(self.firstname), str(self.lastname))

class Student(Person):
    pass

x = Person("John","Doe")
x.printname()

s = Student("Mike","Olsen")
s.printname()