# classwork 1
def points(games):
    total_points = 0
    for game in games:
        x, y = game.split(":")
        if int(x) > int(y):
            total_points += 3
        elif int(x) == int(y):
            total_points += 1
    return total_points  

games = ["3:1", "2:2", "0:1", "4:0", "1:1", "0:0", "3:3", "2:1", "1:0", "4:4"]
print(points(games))  

# classwork 2
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

binary_age = ''
while age > 0:
    binary_age = str(age % 2) + binary_age
    age = age // 2

print(f"თქვენი ასაკი ორობით სისტემაში: {binary_age}")

# classwork 3
def fake_bin(x):
    result = []
    for digit in x:
        if int(digit) < 5:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

print(fake_bin("3456789"))  

# classwork 4
def dna_to_rna(dna):
    rna = ''
    for nucleotide in dna:
        if nucleotide == 'T':
            rna += 'U'
        else:
            rna += nucleotide
    return

print(dna_to_rna("GCAT"))