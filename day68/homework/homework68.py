# 1. რიცხვების გაორმაგება
double = lambda x: x * 2

# 2. სტრინგის სიგრძის გამოთვლა
string_length = lambda s: len(s)

# 3. კენტ რიცხვთა ამოცნობა
is_odd = lambda x: x % 2 != 0

# 4. რიცხვების კვადრატში აყვანა
square = lambda x: x ** 2

# 5. ლუწი რიცხვების კვადრატში აყვანა სიიდან
def even_squares(lst):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst)))

# მაგალითები:
print(double(5))                # 10
print(string_length("hello"))  # 5
print(is_odd(7))               # True
print(square(4))              # 16
print(even_squares([1, 2, 3, 4, 5, 6]))  # [4, 16, 36]
