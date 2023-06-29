class CtxMan:
    def __init__(self, original_fun, new_fun):
        self._bkp_fun = original_fun
        self._new_fun = new_fun

    def __enter__(self):
        global print
        print = self._new_fun

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self._bkp_fun


def check_print(z):
    assert z == 30


def sumfun(x, y):
    print(x + y)


with CtxMan(original_fun=print, new_fun=check_print):
    sumfun(10, 20)

print("Тест пройден")

# assert sumfun(10, 20) == 30

