def decorate(func):
    def inner(*args, **kwargs):
        print("========")
        res = func(*args, **kwargs)
        print("========")
        return res
    return inner


@decorate
def prosto():
    print("Hi")


@decorate
def fun(x, y):
    return x + y


print(prosto())
print(fun(1, 2))
