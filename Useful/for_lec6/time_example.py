import time


start = time.time()
a = 0
for i in range(1, 100000):
    a += i
stop = time.time()
print(stop - start)
