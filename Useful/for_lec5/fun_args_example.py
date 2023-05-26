def summator(*args):
    s = 0
    for i in args:
        s += i
    #print(s)
    return s


result = summator(10, 20, 30, 40, 50, 70)
print(result)


