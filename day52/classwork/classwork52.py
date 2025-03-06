# classwork 1
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = int(sq ** 0.5)  
    return (root + 1) ** 2 if root * root == sq else -1

    return -1

# classwork 2
def min_max(lst):
    min_value = lst[0]
    max_value = lst[0]
    
    for num in lst:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return [min_value, max_value]

# classwork 3
def series_sum(n):
    # Happy Coding ^_^
    sum = 0
    for x in range(n):
        sum = sum + 1/(3 * x + 1)
    return "%.2f" % sum
