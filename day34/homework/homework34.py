# homework 1
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0], my_tuple[1])

# homework 2
numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)
print("same numbers: ", numbers.count(23))

# homework 3
aura = (10, 25, 5, 80, 70, 20) 
for number in aura:
    if number > 10:
        print(number)
    
# homework 4
#  List-ს აქვს უფრო მეტი ფუნქცია რადგან იგი mutable-ია მაგალითად, list-ის ელემენტების დამატება წაშლა და შეცვლა
#  Tuple უფრო სწრაფია შესრულებაში რადგან იგი immutable-ია რაც ნიშნავს რომ მისი ცვლილება არ საჭიროებს დამატებითი რესურსების გამოყენებას
#  Tuple-ს ხშირად იყენებენ ისეთი მონაცემების დასაცავად რომლებიც არ უნდა შეიცვალოს ხოლო list ძირითადად გამოიყენება მონაცემების მენეჯმენტისთვის სადაც ცვლილებები და გამეორება საჭიროა

# homework 5 
# Python-ში mutable და immutable აღნიშნავენ თუ რამდენად შეიძლება შეცვალოს ობიექტის შიგთავსი მას შემდეგ რაც იგი შეიქმნება