text = "Получившаяся строка: "


while (number := input("Введите число: ").lower()) != "stop":
    if number.isdigit():
        text += number
        print(text)
    else:
        print("Вы ввели не числовое значение, пожалуйста введите новый символ")
