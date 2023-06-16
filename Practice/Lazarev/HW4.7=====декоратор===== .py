def my_decorator(func):

    def equals(x):
        return '===========' + func(x) + '==========='
    return equals

@my_decorator
def anyfunc(y):
    return (y)

print(anyfunc('привет'))

