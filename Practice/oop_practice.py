class MyClass:
    x = 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(abc):
        print("Hello my name is "+ abc.name)

class EmptyClass:
    # class definitions cannot be empty, but if you for some reason have
    # a class definition with no content, put in the pass statement to avoid getting an error.
    pass

def sample1():
    pass

# p1 = Person("John", 36)
#
# print(p1)

# print(MyClass)
#
# p1 = MyClass
#
# print(p1.x)print(MyClass)
#
# p1 = MyClass
#
# print(p1.x)