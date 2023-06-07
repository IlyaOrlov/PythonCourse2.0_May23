def decorator(func):
    def wrapper(*args, **kwargs):
        print("===========")
        result = func(*args, **kwargs)
        print("===========")
        return result
    return wrapper

# Пример использования декоратора
@decorator
def example_function():
    print("Функция example_function была вызвана.")

example_function()
