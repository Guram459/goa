# classwork 1
def digitize(n):
    result = []
    while n > 0:
        result.append(n % 10)  
        n = 10               
    return result if result else [0]

print(digitize(35231))  
print(digitize(0))

# classwork 2 
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

print(is_anagram("foefet", "toffee"))        
print(is_anagram("Buckethead", "DeathCubeK")) 
print(is_anagram("Hello", "Olelh"))           
print(is_anagram("Test", "Taste"))

# classwork 3
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# classwork 4
def filter_list(l):
    result = []
    for item in l:
        if type(item) == int:
            result.append(item)
    return result