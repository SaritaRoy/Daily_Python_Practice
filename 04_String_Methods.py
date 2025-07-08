#python offers multiple ways to format strings
name = "sarita"
age = 20
#Using format
print("My name is {} and I am {} years old.".format(name, age))

#Using f- string (Python 3.6+)
print(f"My name is {name} am I am {age} year old.")

a = len(name)
print(a)

#Common string methods
text = "Hello World"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
