import time

def cache(func):
    cache_data = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_data:
            print(f"Кэш: Возврат результата для {key}")
            return cache_data[key]
        else:
            print(f"Кэш: Вычисление результата для {key}")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result
    return wrapper

@cache
def heavy_computation(a, b):
    time.sleep(1)
    return a * b + 10

print(f"Вызов 1: {heavy_computation(2, 3)}")
print(f"Вызов 2: {heavy_computation(4, 5)}")
print(f"Вызов 3: {heavy_computation(2, 3)}")
print(f"Вызов 4: {heavy_computation(4, 1)}")