# classwork 1
def password(st):
    has_upper = False
    has_lower = False
    has_digit = False
    
    if len(st) < 8:
        return False
    
    for char in st:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if has_upper and has_lower and has_digit:
        return True
    
    return False

print(password("Password1"))  
print(password("password1"))  
print(password("Password"))  
print(password("Pass1"))      
print(password("PASSWORD1")) 

# classwork 2
def is_isogram(string):
    string = string.lower()
    
    seen = set()
    
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    
    return True

print(is_isogram("Dermatoglyphics"))  
print(is_isogram("aba"))  
print(is_isogram("moOse"))

# classwork 3
def friend(x):
    result = []  
    for name in x:
        if len(name) == 4:  
            result.append(name)  
    return result

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))  
print(friend(["Peter", "Stephen", "Joe"])) 

# classwork 4
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if not char.isdigit():
                return False
        return True
    return False

print(validate_pin("1234"))   
print(validate_pin("12345"))  
print(validate_pin("a234"))   
print(validate_pin("123456")) 
