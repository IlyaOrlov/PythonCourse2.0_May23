def fun(name_file, par='tabtospace'):
    d = {'\t': '    ', '    ': '\t'}
    if par in {'tabtospace', 'spacetotab'}:
        with open(name_file, 'r') as f:
            res = f.read()
        if par == 'spacetotab':
            res = res.replace('    ', d['    '])
        elif par == 'tabtospace':
            res = res.replace('\t', d['\t'])

        with open(name_file, 'w') as f:
            f.write(res)
    else:
        print('неверный входной параметр')


name = 'my.txt'
fun(name, 'spacetotab')
