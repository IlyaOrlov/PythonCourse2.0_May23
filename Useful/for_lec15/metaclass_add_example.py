class MyMetaClass(type):
    def __add__(cls, other):
        power = cls.power + other.power
        c = MyMetaClass(cls.__name__, tuple(), {'power': power})
        return c


class MyClass(metaclass=MyMetaClass):
    power = 10

    def __add__(self, other):
        c = MyClass()
        c.power = self.power + other.power
        return c


m = MyClass + MyClass
print(m)  # <class '__main__.MyClass'>
print(m.power)  # 20

