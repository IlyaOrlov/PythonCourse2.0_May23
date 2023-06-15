def wrapper(fun):
    def new_fun(*args, **kwargs):
        print('==========')
        res = fun(*args, **kwargs)
        print(res)
        print('==========')
        return res
    return new_fun


def sum(x, y):
    return x + y


sum = wrapper(sum)
sum(2, 5)
