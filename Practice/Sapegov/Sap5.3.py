def chainger_str(x, y):
    for i, j in x.items():
        if i in y:
            y = y.replace(i, j)
    return y


str1 = 'балет привет омлет причал'
d = {'ет': 'етище', 'пр': 'ПР', 'л': 'ллл'}
print(chainger_str(d, str1))
