class Base(type):
    _obj = None

    def __call__(cls, *args, **kwargs):
        print('call of Base called')
        if cls._obj is None:
            cls._obj = super(Base, cls).__call__(*args, **kwargs)
        return cls._obj


class MyClass(metaclass=Base):
    pass


print("start")
ex1 = MyClass()
print("___1")
ex2 = MyClass()
print("___2")
print(f"{id(ex1)=}")
print(f"{id(ex2)=}")

