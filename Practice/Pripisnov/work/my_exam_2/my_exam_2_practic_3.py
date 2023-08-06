def my_format(string, *args, **kwargs):
    if args:
        for i, arg in enumerate(args):
            string = string.replace("{}", str(arg), 1)
    if kwargs:
        for key, value in kwargs.items():
            string = string.replace("{" + str(key) + "}", str(value), 1)
    return string


# Пример использования
name = "Алексей"
age = 30
message = "Привет, меня зовут {} и мне {}. Меня зовут {name} и мне {age}."
res = my_format(message, name, age=age)
#res = my_format(message, name, age, name=name, age=age)
print(res)
