# classwork 1
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

print(count_by(1, 10))  
print(count_by(2, 5))   

# classwork 2
def get_planet_name(id):
    planet_dict = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planet_dict.get(id, "")

print(get_planet_name(3))  
print(get_planet_name(5)) 

# classwork 3
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    
    elif human_years == 2:
        return [2, 24, 24]
    
    cat_years = 24 + (human_years - 2) * 4
    dog_years = 24 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))  
print(human_years_cat_years_dog_years(5))

# classwork 4
def twice_as_old(dad_years_old, son_years_old):
    return abs(2 * son_years_old - dad_years_old)

print(twice_as_old(40, 10))  
print(twice_as_old(50, 15))  
print(twice_as_old(30, 5))  

# classwork 5
def greet(language):
    greetings = [
        ("english", "Welcome"),
        ("czech", "Vitejte"),
        ("danish", "Velkomst"),
        ("dutch", "Welkom"),
        ("estonian", "Tere tulemast"),
        ("finnish", "Tervetuloa"),
        ("flemish", "Welgekomen"),
        ("french", "Bienvenue"),
        ("german", "Willkommen"),
        ("irish", "Failte"),
        ("italian", "Benvenuto"),
        ("latvian", "Gaidits"),
        ("lithuanian", "Laukiamas"),
        ("polish", "Witamy"),
        ("spanish", "Bienvenido"),
        ("swedish", "Valkommen"),
        ("welsh", "Croeso")
    ]

    if not language or not isinstance(language, str):
        return "Welcome" 

    language = language.lower()

    for lang, greeting in greetings:
        if lang == language:
            return greeting  
        
    return "Welcome"

print(greet("french"))   
print(greet("german"))   
print(greet("swedish"))  
print(greet("spanish"))  

print(greet("FRENCH"))   
print(greet("GERMAN"))   

print(greet(""))         
print(greet(None))       
print(greet("japanese")) 
