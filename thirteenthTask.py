import random

secret = random.randint(1, 100)
while True:
    guess = int(input("Введите число: "))
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадали!")
        break