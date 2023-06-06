def outer_fun(fun):
    def inner_fun(*args, **kwargs):
        print('=========')
        res = fun(*args, **kwargs)
        print('=========')
        return res
    return inner_fun


@outer_fun
def super_fun():
    print('Какая-то функция')


# super_fun = outer_fun(super_fun)
super_fun()
