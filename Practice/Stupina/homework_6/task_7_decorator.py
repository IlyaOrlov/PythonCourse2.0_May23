def wrapper(fun):
#здесь же должны быть 2 строки пустые (отделяем ф-ию верхнего уровня)?

    def new_fun(*args, **kwargs):
        print('==========')
        res = fun(*args, **kwargs)
        print(res)
        print('==========')
        return res

    return new_fun
#  а здесь одна?
def sum(x, y):
    return x + y


sum = wrapper(sum)
sum(2, 5)
