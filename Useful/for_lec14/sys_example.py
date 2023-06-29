import sys
sys.path.append("../tmp")
import tmp


# print(tmp.fun(10, 20))
print(sys.byteorder)
print(sys.platform)
# print([i for i in range(sys.maxsize + 1)])  # не хватит памяти;)
print(f"{sys.version=}")
print(f"{sys.version_info=}")
