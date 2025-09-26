surname = input("Введите фамилию: ").strip().title()
name = input("Введите имя: ").strip().title()
patron = input("Введите отчество: ").strip().title()

init = f"{name[0]}.{patron[0]}."

print(f"{surname} {init.upper()}")