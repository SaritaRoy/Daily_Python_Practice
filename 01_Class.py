# Class: A class is a blueprint or a template.
# Example: A form template for an exam that includes fields like name, age, elective, father's name, etc.

# Object: A specific instance created from the class.
# Example: A form filled with John Doe's details.

class Employee:
    company = "HP"  # Class variable shared by all instances

    def get_salary(self):  # Method to get the salary
        print(self)        # Prints the object reference
        return 34000       # Returns a fixed salary

# Creating object 'e' of class Employee
e = Employee()
print(e.get_salary)  # Prints the method reference (not calling it yet)

# Now calling the method
print(e.get_salary())  # Calls the method and prints returned salary

# Creating another object 'e2' of class Employee
e2 = Employee()
print(e2.get_salary())  # Calls the method for e2 and prints returned salary
 