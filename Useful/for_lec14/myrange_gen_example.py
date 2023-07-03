def myrange(start=0, stop=None, step=1):
    if not stop:
        stop = start
        start = 0
    if step == 0:
        f = lambda a, b: False
    elif step > 0:
        f = lambda a, b: a < b
    else:
        f = lambda a, b: a > b
    i = start
    j = 0
    while f(i, stop):
        yield i
        i += step
        j += 1


# for r in myrange(1,10,1):
#     print(r)
g = myrange(1,10,1)
while True:
    print(next(g))