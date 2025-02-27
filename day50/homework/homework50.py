# homework 2
def lovefunc(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return False
    elif a % 2 != 0 and b % 2 == 0:
        return True
    elif a % 2 == 0 and b % 2 != 0:
        return True
    else:
        return False
    
# homework 3
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b > c and a + c > b and c + b > a
    return False

# homework 4
def longest(s1, s2):
    x=''
    y=sorted(s1+s2)
    
    for i in y:
      if i not in x:
        x += i
        
    return x 

# homework 5
def invert(lst):
    return [-x for x in lst]
    pass

# homework 6
def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

# homework 7
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

# homework 8
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)

# homework 9
def dna_to_rna(dna):
    rna = ''
    for nucleotide in dna:
        if nucleotide == 'T':
            rna += 'U'
        else:
            rna += nucleotide
    return rna

# homework 10
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"