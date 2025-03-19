# classwork 1
def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo < limit:
        return "ლუიზა: ნუგზარი აღარ დალიო მეტი"
    else:
        return "ნუგზარი: მოდი ახლა მართლა დამილოცნიე"

print(nugzar_chubinidze(10, 15))
print(nugzar_chubinidze(1, 2))

# classwork 2
def yuri_gagarini():
    pressure = int(input("ჩაწერეთ თქვენი გულის წნევა: "))
    pulse = int(input("ჩაწერეთ თქვენი პულსი: "))
    
    yuri_წნევა = 120
    yuri_პულსი = 80
    
    if pressure == yuri_წნევა and pulse == yuri_პულსი:
        return True
    else:
        return False

result = yuri_gagarini()
print(result)

# classwork 3
def captainjack(gold_coin):
    ships = [150, 200, 250, 300, 350]
    
    choice = int(input("აირჩიეთ გემის ნომერი (1-5): "))
    
    if choice < 1 or choice > 5:
        print("არასწორი არჩევანი!")
        return

    ship_price = ships[choice - 1]
    
    if gold_coin >= ship_price:
        print(f"თქვენი გემის ყიდვა წარმატებით განხორციელდა!")
    else:
        print("ეკიპაჟი აჯანყდება! არ გყოფნით საკმარისი ოქროს მონეტები.")
        
gold_coin = int(input("შეიყვანეთ ოქროს მონეტების რაოდენობა: "))
captainjack(gold_coin)


# classwork 4
apples = ["პანტა", "პანტა", "გორული", "გორული", "პანტა"]

unique_apples = (set(apples))

print(unique_apples)

# classwork 5
def solve(s):
    lower_count = 0
    upper_count = 0
    
    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()
