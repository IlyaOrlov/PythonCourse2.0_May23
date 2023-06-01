text = "Получившаяся строка: "


while (number := input("Введите число: ").lower()) != "stop":
    if number.isdigit():
        text += number
    else:
        print("Вы ввели не числовое значение, пожалуйста введите новый символ")
print(text)
