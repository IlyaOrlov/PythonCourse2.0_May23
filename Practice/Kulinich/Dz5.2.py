def duplikate(lst):
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] == lst[j]:
                return lst[i]

arr = [0,3,24,2,3,7]
print(f"Первый повторившийся символ {duplikate(arr)}")