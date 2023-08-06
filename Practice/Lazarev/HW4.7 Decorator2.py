# Написать декоратор, выводящий "===========" до и после запуска функции
def dec_outer_fun(a):
    def inner_fun(*args, **kwargs):
        print("======")
        res = a(*args, **kwargs)
        print(res)     # только такой споспоб нашёл, чтобы получилось: === (рез) ===
        print("======")
        return res

    return inner_fun


@dec_outer_fun
def anyfunc(x):
    return x ** 2


@dec_outer_fun
def anyfunc2(y):
    return y



res = anyfunc(10) * 2

anyfunc2("hello")
