def texted(x):
    with open(x) as i:
        for y in i:
            yield y


doc = 'ТекстовыйДокумент1.txt'
for j in texted(doc):
    print(j)
