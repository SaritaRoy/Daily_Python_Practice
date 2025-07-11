class Dog:
    # Class variable
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy", 4)

# Accessing instance variables
print("Name:", my_dog.name)          # Buddy
print("Age:", my_dog.age)            # 4

# Calling an instance method
print(my_dog.bark())                 # Buddy says woof!

# Accessing class variable using the instance
print("Species (via instance):", my_dog.species)  # Canis familiaris

# Accessing class variable using the class name
print("Species (via class):", Dog.species)        # Canis familiaris

# Getting the class of the instance
print("Class of my_dog:", my_dog.__class__)       # <class '__main__.Dog'>
