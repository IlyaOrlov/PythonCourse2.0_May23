s = set()
while i := input("Введите значение: "):
    if i in s:
        print("Вы такое уже вводили!")
    else:
        s.add(i)

print(s)



