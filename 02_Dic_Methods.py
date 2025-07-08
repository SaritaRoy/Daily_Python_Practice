# Creating a dictionary
student = {
    "name": "Saru",
    "age": 20,
    "course": "Python"
}

# get() - safely get a value
print(student.get("name"))      # Saru
print(student.get("grade", "N/A"))  # N/A

# keys() - get all keys
print(student.keys())           # dict_keys(['name', 'age', 'course'])

# values() - get all values
print(student.values())         # dict_values(['Saru', 20, 'Python'])

# items() - get all key-value pairs
print(student.items())          # dict_items([('name', 'Saru'), ('age', 20), ('course', 'Python')])

# update() - update values
student.update({"age": 21, "grade": "A"})
print(student)

# pop() - remove by key
student.pop("course")
print(student)

# popitem() - removes the last item (Python 3.7+)
student.popitem()
print(student)

# setdefault() - set default if key not present
student.setdefault("city", "Dehradun")
print(student)

# clear() - removes all items
student.clear()
print(student)
