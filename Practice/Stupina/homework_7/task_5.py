def fun(name_file, par='tabtospace'):
    d = {'\t': '    ', '    ': '\t'}
    with open(name_file, 'r') as f:
        res = f.read()
    if par == 'spacetotab':
        res = res.replace('    ', d['    '])
    elif par == 'tabtospace':
        res = res.replace('\t', d['\t'])
    else:
        print('неверный входной параметр')

    with open(name_file, 'w') as f:
        f.write(res)


name = 'my.txt'
fun(name, 'spacetotab')
