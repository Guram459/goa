# homework 1
def sum_mix(arr):
    return sum(int(x) for x in arr)

# homework 2
def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

print(double_char("String"))      
print(double_char("Hello World"))
print(double_char("1234!_ "))  

# homework 3
def array_plus_array(arr1, arr2):
    total = 0
    for num in arr1:
        total += num
    for num in arr2:
        total += num
    return total

print(array_plus_array([1, 2, 3], [4, 5, 6]))  
print(array_plus_array([10, 20], [30, 40]))   

# homework 4
def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)  
    return ' '.join(reversed_words)

print(reverse_words("The greatest victory is that which requires no battle"))

# homework 5
def sum_str(a, b):
    if not a: a = "0"
    if not b: b = "0"
    
    return str(int(a) + int(b))


print(sum_str("4", "5"))   
print(sum_str("34", "5")) 
print(sum_str("", ""))     
print(sum_str("2", ""))    
print(sum_str("-5", "3"))  