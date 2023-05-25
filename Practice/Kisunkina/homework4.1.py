import random


x = random.randint(1, 100)
print(f"Рандомное число для проверки работы программы: {x}")

if x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
elif x % 15 == 0:
    print("FizzBuzz")
else:
    print(f"{x}")
