def zamena(x, y):
    for key, value in y.items():
        shablon = "{" + key + "}"
        x = x.replace(shablon, str(value))

    return x


# Пример использования
строка_шаблон = "Здравствуйте, {имя}! познает {имя2} ."
данные = {
    "имя": "Елена",
    "имя2": "Pyton"
}
результирующая_строка = zamena(строка_шаблон, данные)
print(результирующая_строка)