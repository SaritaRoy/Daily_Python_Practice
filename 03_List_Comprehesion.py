#Create a list conaining the table of 5
a = 5
table = []

for i in range (1,110):
    table.append(5*1)

table = [5*i for i in range(1,11)]

print(table)

#Write a list comprehension to get the multiples of 3 from 1 to 30.
multiples_of_3 = [x for x in range(1, 31) if x % 3 == 0]
print(multiples_of_3)
