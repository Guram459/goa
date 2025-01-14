# homework 1
# Create initial sets
set_1 = {10, 20, 30, 40}
set_2 = {30, 40, 50, 60}

print("Initial sets:")
print("set_1:", set_1)
print("set_2:", set_2)

# 1 Adding elements with .add()
set_1.add(50)  
print("\nAfter adding 50 to set_1:", set_1)

# 2 Removing elements with .remove()
set_1.remove(20) 
print("\nAfter removing 20 from set_1:", set_1)

# 3 Clearing the set with .clear()
set_1.clear()  
print("\nAfter clearing set_1:", set_1)


set_1 = {10, 20, 30, 40}

# 4 Difference of sets using .difference()
difference_set = set_1.difference(set_2) 
print("\nDifference between set_1 and set_2:", difference_set)

# 5 Union of sets using .union()
union_set = set_1.union(set_2)  
print("\nUnion of set_1 and set_2:", union_set)

# homework 2
student_info = {
    "guram":"name",
    "gelauri":"surname",
     15 :"age",
     100:"minimum_grade"
}

key = student_info.keys()
print("student guram gelxauri info: ", key)

# hoemwork 3
students_data = {
    "name" : "guram",
    "surname" : "gelxauri",
    "year" : 2009
}

x = students_data.values()
print(x)

# homework 4
def AddToDatabase(first_name, last_name, age):
    database = {}
   
    database["first_name"] = first_name
    database["last_name"] = last_name
    database["age"] = age

    print(database)

AddToDatabase("guram", "gelxauri", 15)
