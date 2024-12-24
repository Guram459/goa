#problem 1
def string_to_array(s):
    return s.split()

print(string_to_array("Robin Singh"))
print(string_to_array("I love arrays they are my favorite"))

#problem 2
def string_to_number(s):
    return int(s)

#problem 3
def string_to_number(s):
    return int(s)

#problem 4
def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result

#problem 5
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"


