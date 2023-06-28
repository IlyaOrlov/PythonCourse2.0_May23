t = (10, 20, 30)
lst = [100, 300, 400]
d = {"one": 1}


super_lst = [t, lst, d]

for el in super_lst:
    for i in el:
        print(i)
