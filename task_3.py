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

if len(numbers) < 2:
    print("Недостаточно чисел для нахождения второго по величине.")
else:
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif (second_largest is None or num > second_largest) and num != largest:
            second_largest = num

    if second_largest is not None:
        print(f"Второе по величине число: {second_largest}")
    else:
        print("Не удалось найти второе по величине уникальное число.")