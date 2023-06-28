class MyClass:
    __slots__ = ("attr", "attr1", )

    def __init__(self):
        self.attr = "A"


m = MyClass()
print(dir(m))
m.attr1 = "B"  # m.__dict__["attr1"] = "B"
print(m.__dict__)
print(MyClass.__dict__)
