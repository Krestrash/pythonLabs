seconds = int(input("Введите количество секунд: "))
m, s = divmod(seconds, 60)
print(f"{m} мин {s} сек")