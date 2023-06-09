def outer(fun):
    def inner(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res
    return inner


@outer
def fun():
    print("Привет!")


@outer
def fun1(x, y):
    return x + y

print(fun())
print(fun1(5, 10))
