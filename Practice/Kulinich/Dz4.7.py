def dec_mydec(fun):
    def my_dec(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res
    return my_dec

@dec_mydec
def hello():
    print("Hello World")

hello()

