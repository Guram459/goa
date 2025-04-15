# homework 1

class Car:
    def __init__(self, name, model, age):
        self.name = name
        self.model = model
        self.age = age

    def car_info(self):
        return f"car name is {self.name} and model is {self.model} and age of the car is {self.age}"
    
car = Car("mersedes", "C-class", 32)

print(car.car_info())

# homework 2

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self, name, age, grade):
        return f"{self.name} {self.age} {self.grade}"
    
    def is_passing(self):
        if self.grade >= 5:
            print("you passed this test")
        else:
            print("you didin't pass")

grade = Student("guram", "15", 5)
print(grade.is_passing())

# homework 3

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        if self.age <= 1:
            print("Woof!🐶")
        else:
            print("NO Woof!")

bark = Dog("lesi", 2)
print(bark.bark())

# homework 4

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
areat = Rectangle(15, 10)
print(areat.area())
       
# homework 5

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        return f"Book title is {self.title} and author of this book is {self.author} and it was relised in {self.year}"
    
book = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", "12-საუკუნეში")
print(book.book_info())