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


res = anyfunc(10) * 2
print(res)             # принт только для вывода верного результата


@dec_outer_fun
def anyfunc2(y):
    return y


anyfunc2("hello")

# Не понимаю почему в коде декоратора рез 100, а не 200, и как это исправить
# ======
# 100
# ======
# 200
# ======
# hello
# ======