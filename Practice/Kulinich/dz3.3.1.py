# зашифровка
code = input("Введие пароль    ")
key = 5961
result = (int(code)^int(key))
print(f"Ваш секретный код:  {result}")
