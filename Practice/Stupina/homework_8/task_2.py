def my(name):
    with open(name, encoding='utf-8') as f:
        for res in f:
            yield res
            print('---')


f_name = '1.txt'
for i in my(f_name):
    print(i)
