import threading

def fun(x, y):
    return x + y

def add3(arg_new):
    for args in arg_new:
        x, y = args
        res = fun(x, y)
        print(f'{x} + {y} = {res}')

def add_integer(a):
    int_thr = threading.Thread(target=add3, args=(a,))
    int_thr.start()

def add_string(b):
    str_thr = threading.Thread(target=add3, args=(b,))
    str_thr.start()

def add_list(c):
    l_thr = threading.Thread(target=add3, args=(c,))
    l_thr.start()

a = [(1, 2), (3,4)]
b = [('hello', 'bye'), ('Ivan', 'Maria')]
c = [([1, 2], [3, 4]), (['abc'], ['def'])]

add_integer(a)
add_string(b)
add_list(c)
