def outer(fun):
    def inner(*args, **kwargs):
        print('=========')
        res = fun(*args, **kwargs)
        print('=========')
        return res
    return inner


@outer
def s_fun():
    print("Hello")


s_fun()