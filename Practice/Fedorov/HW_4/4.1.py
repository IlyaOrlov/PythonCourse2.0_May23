# Лист кратных значений
krat = [3, 5, 15]
# Лист выводимых значений кратных листу krat
dan = ["Fizz", "Buzz", "FizzBuzz"]
num = 1
while num < 101:
    x = ""
    for i in krat:
        if num % i == 0:
            x += f"{dan[krat.index(i)]}; "

    if x == "":
        print(num)
    else:
        print(x)
    num += 1
