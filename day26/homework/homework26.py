#homework 1 ვერ გავიგე

#homework 2
def hello_world():
    print("hello_world")

#homework 3
def even_or_odd(number):
    if number % 2 == 0:
        print("არ არის კენტი")
    else:
        print("კი არის კენტი")

#homework 4
def draw_shapes():
    shapes = [
        "******\n******\n******",
        "     *\n    ***\n  *******\n***********\n     *\n     *",
        "*******\n *******\n  ********\n    ********"
    ]
    
    for shape in shapes:
        print(shape)
        print("\n")

draw_shapes()

hello_world()

even_or_odd(23)  

draw_shapes()