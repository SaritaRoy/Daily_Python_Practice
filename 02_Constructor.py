#A constructor is a special method in a class that automatically runs when you create an object.
#In Python, this method is called __init__().
class Student:
    def __init__(self, name, age):
        self.name = name    # setting value using constructor
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object with constructor
s1 = Student("Sara", 21)
s1.display()

s2 = Student("John", 22)
s2.display()
