import time

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                arg_list = []
                for arg in args:
                    arg_list.append(repr(arg))
                for key, value in kwargs.items():
                    arg_list.append(f"{key}={repr(value)}")

                log_entry = f"Время: {current_time}, Функция: {func.__name__}, Аргументы: ({', '.join(arg_list)})"

                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(log_entry + "\n")

                print(f"Лог записан в файл {filename}: {log_entry}")
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Ошибка при логировании или выполнении функции: {e}")
                raise

        return wrapper

    return decorator


@log_calls("function_calls.log")
def calculate_sum(a, b, c=1):
    return a + b + c


print(f"Результат (5, 3): {calculate_sum(5, 3)}")
print(f"Результат (1, 1, c=5): {calculate_sum(1, 1, c=5)}")
