class Enumerate:
    def __init__(self, lst):
        self._i = 0
        self._lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(lst):
            res = self._i, self._lst[self._i]
            self._i += 1
            return res   # (0, 1)
        else:
            raise StopIteration


lst = [1, 2, 3, 4, 5]
for i in Enumerate(lst):
    print(i)

# (0, 1)
# (1, 2)
# (2, 3)
# ...
