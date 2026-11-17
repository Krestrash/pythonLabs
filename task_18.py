from datetime import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, "a", encoding="utf-8") as f:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{time} | {func.__name__} | args={args} kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_calls("calls.log")
def add(a, b):
    return a + b

print(add(2, 3))
