a = 4
b = 2
c = 1

average = (a + b + c)/3.0
print(average)

a1 = 6
b1 = 7
c1 = 12

average1 = (a1 + b1 + c1)/3
print(average)

#Function - def()-help in resuability and modularity in python.

def average(a, b, c):
    d = (a + b + c)/3.0
    print(d)
    average(3, 5, 1)