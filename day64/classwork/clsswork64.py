# # classwork 1

def minimum(arr):
    #your code here...
    return min(arr)

def maximum(arr):
    #...and here
    return max(arr)

# # classwork 2

def make_upper_case(s):
    return s.upper()


# # classwork 3
class MyCat:
    x = "🐈‍"

p1 = MyCat()

print(p1.x)

# classwork 4

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self, name, surname, age):
        return f"{self.name} {self.surname} {self.age}"
    
    def my_age(self):
        return f" მე ვარ {self.age} წლის"

p2 = Human("guram", "Gelxauri", 15)

print(p2.name, p2.surname, p2.age)
print(p2.my_age())

# classwork 5
 
class Human1:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self, name, surname, age):
        return f"{self.name} {self.surname} {self.age}"
    
    def my_name(self):
        return f" მე მქვია {self.name}"
    
    def my_surname(self):
        return f" ჩემი გვარი {self.surname}"
    
    def my_age(self):
        return f" მე ვარ {self.age} წლის" 
    
p3 = Human1("guram", "Gelxauri", 15)

print(p3.name, p3.surname, p3.age)  
print(p3.my_name())
print(p3.my_surname())
print(p3.my_age())

