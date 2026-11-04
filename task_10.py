sum = int(input("Enter sum "))
age = int(input("Enter age "))
is_birthday = bool(int(input("Is it your birthday today(0 - no, 1 - yes) ")))
vip = bool(int(input("Are you VIP(0 - no, 1 - yes) ")))
discount = 0


if sum > 1000 and not vip:
    discount += 10
if age>=63:
    discount +=5
if vip:
    discount +=15
if is_birthday:
    discount +=5

if discount >25:
    discount  = 25       

print("Ваша скидка "+ str(discount))    
