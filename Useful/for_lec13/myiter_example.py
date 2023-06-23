class MyIter:
    def __init__(self, n, m):
        self._i = n if n % 2 == 0 else n + 1
        self._num = 0
        self._max_num = m

    def __iter__(self):
        return self

    def __next__(self):
        if self._num < self._max_num:
            res = self._i
            self._num += 1
            self._i += 2
            return res
        else:
            raise StopIteration


# m = MyIter(2, 1000000)
# it = iter(m)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


for i in MyIter(2, 1000000):
    print(i)

