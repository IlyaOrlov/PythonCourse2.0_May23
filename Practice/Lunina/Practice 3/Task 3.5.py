import time


print("Давай проверим является ли слово палиндромом \n")
time.sleep(2)
print("Попытка № 1")
a = input("Введите слово: \n")
a1 = a[::-1]
print(f"Зеркалим слово: {a1}")
res = a1 in a
print(f"Ответ программы: {res}\n")
time.sleep(2)

print("Попытка № 2")
b = input("Введите слово: \n")
b1 = b[::-1]
print(f"Зеркалим слово: {b1}")
res = b1 == b
print(f"Ответ программы: {res} \n")
time.sleep(2)

print("Заходите ещё. Good bay.")
