# classwork 1

"sum_array = lambda arr : sum(arr)"

# classwork 2

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"My name is: {self.name}, my surname is: {self.surname}, and I'm {self.age} old"
    

info = ("gurika", "gelxauri", 15)
print(info)

# classwork 4

find_average = lambda number : sum(number) / len(number) if number else 0

# classwork 5

monkey_count = lambda n : list(range(1, n + 1))