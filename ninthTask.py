def valid_ip(ip) -> bool:
    parts = ip.split(".")
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

address = input("Введите IP-адрес: ")
print("Корректный" if valid_ip(address) else "Некорректный")