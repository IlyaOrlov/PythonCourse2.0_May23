def outer_fun(fun):
    def inner_fun(*args, **kwargs):
        print('=========')
        res = fun(*args, **kwargs)
        print('=========')
        return res
    return inner_fun


@outer_fun
def super_fun():
    print('Какое-то выполнение функции')


super_fun()
