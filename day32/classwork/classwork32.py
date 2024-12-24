#problem 1
def opposite(number):
    return -number
 
print(opposite(1))    
print(opposite(14))   
print(opposite(-34))  

#problem 2
def repeat_str(repeat, string):
    return string * repeat

print(repeat_str(6, "მე"))        
print(repeat_str(5, "Gamarjoba"))    

#problem 3
def greet():
    return "hello Georgia!"

#problem 4
def count_sheeps(sheep):
    return sheep.count(True)

sheep = [True, True, True, False,
         False, False, True, True]

print(count_sheeps(sheep))

#problem 5
def litres(time):
    return int(time * 0.5)

print(litres(3))    
print(litres(6.7))  
print(litres(11.8)) 

#problem 6
def litres(time):
    return int(time * 0.5)  


print(litres(3))    
print(litres(6.7))  
print(litres(11.8)) 