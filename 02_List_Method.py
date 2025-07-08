my_list = [10, 20, 30, 40, 50]   # Initial list
my_list.append(50)              # Add 50 at the end → [10, 20, 30, 40, 50, 50]
my_list.insert(2, 25)           # Insert 25 at index 2 → [10, 20, 25, 30, 40, 50, 50]
my_list.remove(40)              # Remove the first 40 → [10, 20, 25, 30, 50, 50]
pooped = my_list.pop()          # Pop last element (50) → [10, 20, 25, 30, 50]
my_list.sort()                  # Sort → [10, 20, 25, 30, 50]
my_list.reverse()               # Reverse → [50, 30, 25, 20, 10]

print(my_list)                  # Output: [50, 30, 25, 20, 10]
