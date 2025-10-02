def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])

            nested_list = lst.pop(i)

            j = len(nested_list) - 1
            while j >= 0:
                lst.insert(i, nested_list[j])
                j -= 1
        else:
            i += 1


list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(f"Исходный список: {list_a}")
flatten_list(list_a)
print(f"Плоский список: {list_a}")