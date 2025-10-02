import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"Функция '{func.__name__}' выполнена за {execution_time_ms:.2f} мс")
        return result
    return wrapper

@timing
def slow_function(n):
    sum_val = 0
    i = 0
    while i < n:
        sum_val += i
        i += 1
    return sum_val

@timing
def fast_function(a, b):
    return a * b

result1 = slow_function(1000000)
result2 = fast_function(10, 20)

print(f"Результат slow_function: {result1}")
print(f"Результат fast_function: {result2}")