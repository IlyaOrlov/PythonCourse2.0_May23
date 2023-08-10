class MyMetaClass(type):
    pass


class MyClass(metaclass=MyMetaClass):
    pass


class MyChildClass(MyClass):
    pass


obj = MyClass()


print(f"{type(obj)=}")
print(f"{type(MyChildClass)=}")