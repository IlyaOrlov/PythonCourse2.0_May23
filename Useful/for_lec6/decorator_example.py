import time

def get_time(fun):
    def new_fun(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        print(f"Время выполнения: {time.time() - start}")
        return res

    return new_fun

@get_time
def sum_fun(x, y):
    res = x + y
    return res

@get_time
def mul_fun(x, y):
    res = x * y
    return res

def sq_fun(x):
    res = x ** 2
    return res


# sum_fun = get_time(sum_fun)
# mul_fun = get_time(mul_fun)
# sq_fun = get_time(sq_fun)

print(sum_fun(10, 20))
print(mul_fun(30, 40))
print(sq_fun(50))
