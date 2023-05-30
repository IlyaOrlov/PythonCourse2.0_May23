def fun_max_1(x, y):
    if x > y:
        print(f'Наибольшее число: {x}')
    elif x < y:
        print(f'Наибольшее число: {y}')
    else:
        print('Числа равны')


def fun_max_2(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        out = 'Числа равны'
        return out


fun_max_1(10, 15)
res = fun_max_2(100, 100)
# print(res)
