passw = input("Введите пароль")

if len(passw) < 16:
    print("Пароль слишком короткий")

elif passw.isdigit() or passw.isalpha():
    print("Слабый пароль")

else:
    print("Надежный пароль")
