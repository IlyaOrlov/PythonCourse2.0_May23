# Написать декоратор, выводящий "===========" до и после запуска функции
def fun_dec(fun):
    def fun_two(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res

    return fun_two


@fun_dec
def fun(x, y):
    a = x + y
    print('Выполнение функции {} происходит внутри декоратора'.format(fun))
    return a


print(fun(20, 20))
