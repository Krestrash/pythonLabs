n = int(input("Введите число: "))
if n % 7 == 0:
    print("Магическое число!")
else:
    print(sum(map(int, str(abs(n)))))