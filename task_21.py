import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        ms = (end - start) * 1000
        print(f" {func.__name__} выполнилась за {ms:.3f} мс")
        return result
    return wrapper


@timing
def add(n):
    s = 0
    for i in range(n):
        s += i
    return s


print(add(1000000))
