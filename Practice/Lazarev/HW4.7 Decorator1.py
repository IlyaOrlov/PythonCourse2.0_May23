def my_dec(t):
    def result(f):
        def add_message(*args, **kwargs):
            r = f(*args, **kwargs)
            print(f'{t} {r} {t}')
            print(f'{t}\n{r}\n{t}')
            return r
        return add_message
    return result


@my_dec('====')
def anyfunc(y):
    return y ** 2

z = anyfunc(10) * 2


@my_dec('====')
def anyfunc2(y):
    return y

anyfunc2("hello")

# Здесь кстати тоже не верный ответ