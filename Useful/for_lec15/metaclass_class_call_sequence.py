# type.__call()__ -> __new__() -> [новый экземпляр появляется в памяти] -> __init__()

class Base(type):
    _obj = None

    def __new__(cls, *args, **kwargs):
        print('new of Base called')
        return super().__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('call of Base called')
        return super(Base, cls).__call__(*args, **kwargs)


class MyClass(metaclass=Base):
    def __new__(cls, *args, **kwargs):
        print('new of MyClass called')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("init of My class called")



print("start")
m = MyClass()