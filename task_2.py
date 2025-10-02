raw_input = input("Введите список чисел через пробел: ")
raw_numbers = raw_input.split()

numbers = []
for num_str in raw_numbers:
    try:
        if '.' in num_str:
            numbers.append(float(num_str))
        else:
            numbers.append(int(num_str))
    except ValueError:
        pass

counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

unique_numbers = []
repeating_numbers = []
for num, count in counts.items():
    is_unique = True
    for existing_unique in unique_numbers:
        if existing_unique == num:
            is_unique = False
            break

    is_repeating = False
    for existing_repeating in repeating_numbers:
        if existing_repeating == num:
            is_repeating = False
            break

    if count == 1 and is_unique:
        unique_numbers.append(num)
    elif count > 1 and not is_repeating:
        repeating_numbers.append(num)

even_numbers = []
odd_numbers = []
negative_numbers = []
float_numbers = []
sum_of_multiples_of_5 = 0
max_number = None
min_number = None

for num in numbers:
    if max_number is None or num > max_number:
        max_number = num
    if min_number is None or num < min_number:
        min_number = num

    if isinstance(num, int) or (isinstance(num, float) and num.is_integer()):
        num_int = int(num)
        if num_int % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        if num_int % 5 == 0:
            sum_of_multiples_of_5 += num_int

    if isinstance(num, float) and not num.is_integer():
        float_numbers.append(num)

    if num < 0:
        negative_numbers.append(num)


print(f"1. Уникальные числа: {unique_numbers}")
print(f"2. Повторяющиеся числа: {repeating_numbers}")
print(f"3. Четные числа: {even_numbers}")
print(f"   Нечетные числа: {odd_numbers}")
print(f"4. Отрицательные числа: {negative_numbers}")
print(f"5. Числа с плавающей точкой: {float_numbers}")
print(f"6. Сумма всех чисел, кратных 5 (только целые числа): {sum_of_multiples_of_5}")
print(f"7. Самое большое число: {max_number}")
print(f"8. Самое маленькое число: {min_number}")