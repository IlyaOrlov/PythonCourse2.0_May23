#Транспонирование матрицы
lst = [
    [1, 2, 3],
    [4, 5, 6]
]
print(f"Исходная матрица{lst}")
#for i in range(len(lst)+1):
   # a.append([0] * len(lst))
a = [[0] * len(lst) for i in range(len(lst)+1)]
print(a)
#for i in range(len(lst)):
   # for j in range(3):
        #a[j][i] = lst[i][j]
a = [[lst[i][j] for i in range(len(lst))] for j in range(len(lst[0]))]
print(a)
