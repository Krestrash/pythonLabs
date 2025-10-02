raw_input_1 = input("Введите первый набор чисел через пробел: ")
raw_input_2 = input("Введите второй набор чисел через пробел: ")


def parse_numbers(raw_input):
    numbers = []
    for num_str in raw_input.split():
        try:
            if '.' in num_str:
                numbers.append(float(num_str))
            else:
                numbers.append(int(num_str))
        except ValueError:
            pass
    return numbers


def get_unique(input_list):
    unique = []
    for item in input_list:
        is_unique = True
        for existing in unique:
            if existing == item:
                is_unique = False
                break
        if is_unique:
            unique.append(item)
    return unique


list_a = parse_numbers(raw_input_1)
list_b = parse_numbers(raw_input_2)

unique_a = get_unique(list_a)
unique_b = get_unique(list_b)

intersection = []
for num_a in unique_a:
    is_in_b = False
    for num_b in unique_b:
        if num_a == num_b:
            is_in_b = True
            break

    is_duplicate_in_intersection = False
    for existing in intersection:
        if existing == num_a:
            is_duplicate_in_intersection = True
            break

    if is_in_b and not is_duplicate_in_intersection:
        intersection.append(num_a)

only_a = []
for num_a in unique_a:
    is_in_b = False
    for num_b in unique_b:
        if num_a == num_b:
            is_in_b = True
            break
    if not is_in_b:
        only_a.append(num_a)

only_b = []
for num_b in unique_b:
    is_in_a = False
    for num_a in unique_a:
        if num_b == num_a:
            is_in_a = True
            break
    if not is_in_a:
        only_b.append(num_b)

symmetric_difference = []
for num in only_a:
    symmetric_difference.append(num)
for num in only_b:
    symmetric_difference.append(num)


print(f"1. Числа, присутствующие в обоих наборах (пересечение): {intersection}")
print(f"2. Числа из первого набора, отсутствующие во втором: {only_a}")
print(f"   Числа из второго набора, отсутствующие в первом: {only_b}")
print(f"3. Числа из обоих наборов, за исключением пересечения (симметричная разница): {symmetric_difference}")
