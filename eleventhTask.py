


day, month = map(int, input("Введите день и месяц рождения (дд мм): ").split())


print(f"Ваши данные: \t  День: {day} \t  Месяц: {month}")
if (month == 3 and day >= 21 ) or ( month == (3 % 12 + 1) and day < 20):
    print("Ваш знак зодиака: Овен")

if (month == 4 and day >=  20 ) or ( month == (4 % 12 + 1) and day < 21):
    print("Ваш знак зодиака: Телец")

if (month == 5 and day >= 21) or ( month == (5 % 12 + 1) and day < 21):
    print("Ваш знак зодиака: Близнецы")

if (month == 6 and day >= 21 ) or ( month == (6 % 12 + 1) and day < 22):
    print("Ваш знак зодиака: Рак")

if (month == 7 and day >= 23 ) or ( month == (7 % 12 + 1) and day < 23):
    print("Ваш знак зодиака: Лев")

if (month == 8 and day >= 23 ) or ( month == (8 % 12 + 1) and day < 23 ):
    print("Ваш знак зодиака: Дева")

if (month == 9 and day >= 23 ) or ( month == (9 % 12 + 1) and day < 23 ):
    print("Ваш знак зодиака: Весы")

if (month == 10 and day >= 23 ) or ( month == (10 % 12 + 1) and day < 22 ):
    print("Ваш знак зодиака: Скорпион")

if (month == 11 and day >= 22 ) or ( month == (11 % 12 + 1) and day < 22):
    print("Ваш знак зодиака: Стрелец")

if (month == 12 and day >= 22 ) or ( month == (12 % 12 + 1) and day < 20):
    print("Ваш знак зодиака: Козерог")

if (month ==  1 and day >= 20 ) or ( month == (1 % 12 + 1) and day < 19 ):
    print("Ваш знак зодиака: Водолей")

if (month == 2 and day >= 19 ) or ( month == (2 % 12 + 1) and day < 20 ):
    print("Ваш знак зодиака: Рыбы")


