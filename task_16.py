def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            inner = lst.pop(i)
            flatten_list(inner)
            for j in range(len(inner)):
                lst.insert(i + j, inner[j])
        else:
            i += 1


list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)
