# classwork 1
def manual_difference(set1, set2):
    result = set1.copy() 
    for item in set2:
        result.discard(item)
    return result
 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

print(manual_difference(set_a, set_b))  

# classwork 2
student_1 = {
    "ასაკი": 16,
    "საშუალო ქულა": 85,
    "სახელი": "guram",
    "გვარი": "gelxauri"
}

student_2 = {
    "ასაკი": 17,
    "საშუალო ქულა": 90,
    "სახელი": "davit",
    "გვარი": "kobaze"
}

print(student_1)
print(student_2) 