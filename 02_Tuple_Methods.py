# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 20)

# ✅ 1. count() – counts how many times a value appears
print("Count of 20:", my_tuple.count(20))  # Output: 3

# ✅ 2. index() – returns the index of the first occurrence of a value
print("Index of 30:", my_tuple.index(30))  # Output: 2

# 🔸 Concatenation – joining two tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated Tuple:", t3)  # Output: (1, 2, 3, 4)

# 🔸 Repetition – repeating a tuple
t4 = t1 * 3
print("Repeated Tuple:", t4)  # Output: (1, 2, 1, 2, 1, 2)

# 🔸 Membership test – checking if value exists
print("Is 20 in my_tuple?", 20 in my_tuple)  # Output: True
print("Is 50 not in my_tuple?", 50 not in my_tuple)  # Output: True

# 🔸 Iteration – looping through tuple elements
print("Elements in my_tuple:")
for item in my_tuple:
    print(item)

# 🔸 Length of tuple
print("Length of my_tuple:", len(my_tuple))

# 🔸 Slicing a tuple
print("Sliced tuple (index 1 to 3):", my_tuple[1:4])
