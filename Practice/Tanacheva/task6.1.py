def fun_decorator(fun1):
    def inner_fun(*args, **kwargs):
        # code before fun1
        print("===========")
        res = fun1(*args, **kwargs)
        # code after fun1
        print("===========")
        return res
    print("===========")
    return inner_fun


@fun_decorator
def fun1(x, y):
    return x+y


print(fun1(10, 20))
