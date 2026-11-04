def cache(func):
    saved = {}

    def wrapper(*args):
        if args in saved:
            print(f"из кэша {args}")
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result

    return wrapper


@cache
def sqr(x):
    print(f"вычисл {x}")
    return x * x


print(sqr(5))
print(sqr(5))
print(sqr(7))
print(sqr(5))
print(sqr(7))
