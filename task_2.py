def merge_dicts(first_dict, second_dict):
    for key, value_b in second_dict.items():
        if key in first_dict:
            value_a = first_dict[key]
            if isinstance(value_a, dict) and isinstance(value_b, dict):
                merge_dicts(value_a, value_b)
            else:
                first_dict[key] = value_b
        else:
            first_dict[key] = value_b

dict_a = {"a": 1, "b": {"c": 1, "f": 4}, "g": [1, 2]}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}, "g": {3, 4}}
print(f"Словарь A до: {dict_a}")
print(f"Словарь B:    {dict_b}")
merge_dicts(dict_a, dict_b)
print(f"Словарь A после слияния: {dict_a}")
