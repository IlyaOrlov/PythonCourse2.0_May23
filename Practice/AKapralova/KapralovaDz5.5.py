def fun_change(name, x):
    with open(name) as f:
        res = f.read()
        if x == 1:
            res = res.replace('    ', '\t')
        else:
            res = res.replace('\t', '    ')
    with open(name, 'w') as f:
        f.write(res)


y = int(input('Введите для четырех пробелов - 1, а для табуляции - 2'))
file = '1txt'
if y == 1 or y == 2:
    fun_change(file, y)
else:
    print('Неверное значение! Введите 1 или 2!')
