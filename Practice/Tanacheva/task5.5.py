def myfun(user_input,filename):
    with open(filename, "r") as f:
        res = f.read()
        if user_input == 1:
            res = res.replace('\t',"    ")
        else:
            res = res.replace("    ","\t")
    with open(filename, 'w') as f:
        f.write(res)


user_input1 = int(input("Выберите условия: 1-заменить все символы табуляции на 4 пробела, 2-заменить 4 пробела на символ табуляции:"))
file1 = '1.txt'

if user_input1 == 1 or user_input1 == 2:
    myfun(user_input1,file1)
else:
    print('Вы ввели неправильную цифру, перезапустите программу')