def zamena(x, y):
    for key, value in y.items():
        shablon = f"{{{key}}}"
        x = x.replace(shablon, str(value))

    return x


   # Пример использования
stroka_shablon = "Здравствуйте, {имя}! познает {имя2} ."
dannie = {
    "имя": "Елена",
    "имя2": "Pyton"
}
rezult = zamena(stroka_shablon, dannie)
print(rezult)