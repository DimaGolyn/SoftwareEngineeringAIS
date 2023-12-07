def dector(fun):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция: {fun.__name__}")
        print(f"Аргументы: {args}, Ключевые аргументы: {kwargs}")
        result = fun(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

# Пример использования декоратора
@dector
def multiply(a, b):
    return a * b
@dector
def greet(name):
    return f"Привет, {name}!"

multiply_result = multiply(3, 3)
greet_result = greet("Друг")