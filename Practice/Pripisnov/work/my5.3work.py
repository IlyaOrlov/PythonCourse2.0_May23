def replace_templates(s, x):
    for key, value in x.items():
        s = s.replace(key, str(value))
    return s


my_string = "Привет, {name}! Сегодня температура {temperature} градусов."
my_templates = {"{name}": "Алексей", "{temperature}": 25}

res = replace_templates(my_string, my_templates)
print("Результат замены:", res)
