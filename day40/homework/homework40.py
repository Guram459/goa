# homework 1
def remove_duplicate_words(s):
    words = s.split()  
    unique_words = [] 

    for word in words:
        if word not in unique_words:
            unique_words.append(word) 

    return ' '.join(unique_words)  

input_string = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
output_string = remove_duplicate_words(input_string)
print(output_string)

# homework 2
def stray(arr):
    unique_number = 0
    for num in arr:
        unique_number ^= num  
    return unique_number

arr = [1, 1, 2]
print(stray(arr))

# homewrok 3
def solution(nums):
    if not nums:  
        return []
    return sorted(nums)  

nums = [1, 2, 3, 10, 5]
print(solution(nums))

# homework 4
def capitals(word):
    indices = [] 
    for i in range(len(word)):  
        if word[i].isupper():  
            indices.append(i)  
    return indices

word = "CodEWaRs"
print(capitals(word))

# homework 5
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result

print(factorial(5))  
print(factorial(0)) 