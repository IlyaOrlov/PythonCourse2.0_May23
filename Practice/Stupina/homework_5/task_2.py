def fun(lst):
    k = set()
    for elem in lst:
        if elem in k:
            return elem
        else:
            k.add(elem)


lst = [0, 12, 120, 10, 12, 4, 4]
print(f'Исходная строка: {lst} \nПервый повторившийся символ: {fun(lst)}')
