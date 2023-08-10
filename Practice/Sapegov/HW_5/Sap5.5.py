def f_change(name, x):
    with open(name) as f:
        res = f.read()
        if x == 1:
            res = res.replace('    ', '\t')
        else:
            res = res.replace('\t', '    ')
    with open(name, 'w') as f:
        f.write(res)


y = int(input('Нажмите 1, если хотите заменить 4 пробела на табуляцию, либо 2, если наоборот: '))
nf = 'for5.5.txt'
if y == 1 or y == 2:
    f_change(nf, y)
else:
    print('Введите 1 или 2')
