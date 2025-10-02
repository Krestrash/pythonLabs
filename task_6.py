def unique_elements(nested_list):
    result = []

    def process_element(element):
        if isinstance(element, list):
            for item in element:
                process_element(item)
        else:
            is_unique = True
            for existing in result:
                if existing == element:
                    is_unique = False
                    break
            if is_unique:
                result.append(element)

    process_element(nested_list)
    return result


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
unique = unique_elements(list_a)
print(f"Исходный список: {list_a}")
print(f"Уникальные элементы: {unique}")
