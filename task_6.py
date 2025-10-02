raw_input = input("Введите список элементов через пробел: ")
input_list = raw_input.split()

unique_list = []

for item in input_list:
    is_duplicate = False
    for unique_item in unique_list:
        if unique_item == item:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list.append(item)

print(f"\nСписок с удаленными дубликатами: {unique_list}")
