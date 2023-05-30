def outer_fun(fun):
    def inner_fun(*args, **kwargs):
        # code before fun
        print("start")
        res = fun(*args, **kwargs)
        # code after fun
        print("finish")
        return res

    return inner_fun


def fun(x, y):
    return x + y


backup = fun
fun = outer_fun(fun)
print(fun(10, 20))
print("===============")
fun = backup
print(fun(10, 20))