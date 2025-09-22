a, b = map(int, input("Введите два числа через пробел: ").split())

print(f"Сумма: {a + b}")
print(f"Разность: {a - b}")
print(f"Произведение: {a * b}")
print(f"Частное: {a / b:.2f}" if b else "Деление на ноль невозможно")
print(f"Остаток: {a % b}" if b else "Остаток не вычисляется")
print(f"Степень: {a ** b}")