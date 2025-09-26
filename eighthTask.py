s = input("Введите строку: ").lower().replace(" ", "")
print("Палиндром" if s == s[::-1] else "Не палиндром")