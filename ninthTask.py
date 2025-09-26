

address = input("Введите IP-адрес: ")
parts = address.split(".")
print("Корректный" if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts) else "Некорректный")