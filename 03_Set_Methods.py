# create two sets
a = {1, 2, 3}
b = {3, 4, 5}

# add element
a.add(4)
print("Add:", a)

# remove element
a.remove(2)
print("Remove:", a)

# union (join both sets)
print("Union:", a | b)

# intersection (common)
print("Intersection:", a & b)

# difference (a - b)
print("Difference:", a - b)

# symmetric difference (not common)
print("Symmetric difference:", a ^ b)

