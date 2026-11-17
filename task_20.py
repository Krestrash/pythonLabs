def unique_elements(lst):
    result = []

    def helper(data):
        for item in data:
            if isinstance(item, list):
                helper(item)
            else:
                if item not in result:
                    result.append(item)

    helper(lst)
    return result   


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
