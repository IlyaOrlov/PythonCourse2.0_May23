m = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]]
d = int(input("Будет удален столбец с цифрой: "))
m[:] = map(lambda y : list(filter(lambda x: y.index(x)%5 != d, y)), m)

print(m[:])
