def chainger_str(x, y):
    str2 = ''
    str3 = ''
    for i in x:
        if i in y:
            str3 = str2.replace(i, d[i])
            str2 = y.replace(i, d[i])
    return str3


str1 = 'балет привет омлет причал'
d = {'ет': 'етище', 'пр': 'ПР'}
print(chainger_str(d, str1))
