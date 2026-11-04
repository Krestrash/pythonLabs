def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(
                        f"Аргумент {i + 1} должен быть {types[i].__name__}, "
                        f"а получен {type(args[i]).__name__}"
                    )
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


print(add(2, 3))
print(add(2, "три"))
