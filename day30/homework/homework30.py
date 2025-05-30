#problem 1
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

#problem 2
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2  
    return total

#problem 3
def sum_array(a):
    return sum(a)

#problem 4
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

#problem 5
def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]

