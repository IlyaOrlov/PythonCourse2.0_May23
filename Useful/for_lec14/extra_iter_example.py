class MyClass:
    def __init__(self, lst, n):
        self._lst = lst[n:]

    def __iter__(self):
        return iter(self._lst)


lst1 = [1, 2, 3]
n = 1
for i in MyClass(lst1, n):
    print(i)


