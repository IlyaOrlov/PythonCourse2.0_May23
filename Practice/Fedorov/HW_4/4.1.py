import random

x = ""
num = random.randint(1, 100)
# Лист кратных значений
krat = [3, 5, 15]
# Лист выводимых значений кратных листу krat
dan = ["Fizz", "Buzz", "FizzBuzz"]
for i in krat:
    if num % i == 0:
        x += f"{dan[krat.index(i)]}\n"

if x == "":
    print(num)
else:
    print(x)
