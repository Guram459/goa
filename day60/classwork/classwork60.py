# classwork 1
def count_arara(n):
    if n == 1:
        return "anane"
    
    result = ['adak'] * (n // 2)
    
    if n % 2 == 1:
        result.append('anane')
        
    return " ".join(result)

# classwork 2
def is_planet_mnemonic_correct(solar_system, mnemonic):
    planet_letters = [planet[0] for planet in solar_system if planet != "Asteroid"]
    mnemonic_letters = [word[0] for word in mnemonic.split()]
   
    return planet_letters == mnemonic_letters

# classwork 3
def max_possible_score(points, new_questions):
    total_score = 0
    
    for question, value in points():
        if question in new_questions:
            total_score += value 
        else:
            total_score += value
    
    return total_score
