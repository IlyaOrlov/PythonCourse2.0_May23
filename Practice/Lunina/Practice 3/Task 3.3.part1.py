import time


print("Здравствуйте, я помощник блокировки ваших активов.")
time.sleep(2)
code = input("Введите ваш код из 4 цифр: ")
code = int(code)
key = 256
res = code ^ key

print("Получившийся код можете отправить своей жене.")
time.sleep(2)

print(f"Процесс завершен.Код: {res}")
