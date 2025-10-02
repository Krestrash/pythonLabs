def merge_sorted_list(first_list, second_list):
    merged_list = []
    i = 0
    j = 0
    len1 = 0
    for _ in first_list:
        len1 += 1
    len2 = 0
    for _ in second_list:
        len2 += 1

    while i < len1 and j < len2:
        if first_list[i] <= second_list[j]:
            merged_list.append(first_list[i])
            i += 1
        else:
            merged_list.append(second_list[j])
            j += 1

    while i < len1:
        merged_list.append(first_list[i])
        i += 1

    while j < len2:
        merged_list.append(second_list[j])
        j += 1

    return merged_list


list1 = [1, 5, 8, 12]
list2 = [2, 3, 9, 10, 15]
merged = merge_sorted_list(list1, list2)
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
print(f"Объединенный отсортированный список: {merged}")