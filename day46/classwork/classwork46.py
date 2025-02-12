# classwork 1
def filter_list(l):
    filtered_list = []
    
    for element in l:
        if type(element) == int:
            filtered_list.append(element)
    
    return filtered_list

# classwork 2
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in string_:
        if char not in vowels:
            result += char
    
    return result

# classwork 3
def descending_order(num):
    num_str = str(num)
    
    count = [0] * 10
    
    for digit in num_str:
        count[int(digit)] += 1
    
    sorted_num = ""
    
    for digit in range(9, -1, -1):
        sorted_num += str(digit) * count[digit]
    
    return int(sorted_num)