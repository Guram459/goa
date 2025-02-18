# classwork 1
def xo(s):
    s = s.lower()
    
    count_x = 0
    count_o = 0
    
    for char in s:
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1
    
    return count_x == count_o

# classwork 2
def find_short(s):
    words = s.split()
    shortest_length = len(words[0])  
    
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
    
    return shortest_length

# classwork 3
def solution(string, ending):
    if len(ending) > len(string):
        return False
    for i in range(1, len(ending) + 1):
        if string[-i] != ending[-i]:
            return False
    return True

# classwork 4
def accum(st):
    result = ""
    for i in range(len(st)):
        char = st[i]
        uppercase_char = char.upper()
        lowercase_part = char.lower() * i
        combined = uppercase_char + lowercase_part
        
        if i > 0:
            result += "-" + combined
        else:
            result += combined  
            
    return result