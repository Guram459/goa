import math

# დავალება 1: Dog Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ობიექტების შექმნა
dog1 = Dog("Max", 5)
dog2 = Dog("Bella", 3)

# დაბეჭდვა
print(f"Dog 1: Name - {dog1.name}, Age - {dog1.age}")
print(f"Dog 2: Name - {dog2.name}, Age - {dog2.age}")


# დავალება 2: Car Class
class Car:
    def drive(self):
        print("The car is driving")
        
    def stop(self):
        print("The car has stopped")

# მანქანის ობიექტის შექმნა
my_car = Car()

# მეთოდების გამოძახება
my_car.drive()
my_car.stop()


# დავალება 3: Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# ობიექტის შექმნა
circle = Circle(5)

# ფართობის დაბეჭდვა
print(f"The area of the circle is: {circle.area()}")


# დავალება 4: Student Class
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}.")

# სტუდენტის ობიექტის შექმნა
student = Student("Giorgi", 10, "Math")

# introduce მეთოდის გამოძახება
student.introduce()


# დავალება 5: BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

# ანგარიშის ობიექტის შექმნა
account = BankAccount(100)

# მეთოდების გამოძახება
account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # საკმარისი თანხა არაა
