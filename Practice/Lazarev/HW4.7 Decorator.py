def my_decorator(func):

    def equals(x):
        return '===========' + func(x) + '==========='
    return equals

@my_decorator
def anyfunc(y):
    return y ** 2
# def anyfunc(y):
#     return (y)
z = anyfunc(10) * 2
