def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(f"Ожидается {len(expected_types)} позиционных аргумента, получено {len(args)}")

            i = 0
            while i < len(args):
                arg = args[i]
                expected_type = expected_types[i]
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Аргумент {i + 1} ('{arg}') имеет тип '{type(arg).__name__}', ожидался '{expected_type.__name__}'")
                i += 1

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


@type_check(str, list)
def print_list_item(prefix, data):
    return f"{prefix}: {data[0]}"



print(f"add(5, 3) = {add(5, 3)}")
print("---")


print(f"print_list_item('Список', ['apple', 'banana']) = {print_list_item('Список', ['apple', 'banana'])}")
print("---")


try:
    add(5, "3")
except TypeError as e:
    print(f"Перехвачено исключение: {e}")
print("---")


try:
    print_list_item(100, ["apple", "banana"])
except TypeError as e:
    print(f"Перехвачено исключение: {e}")
