def transp(arr):
    arrTrans = [[0 for j in range(len(arr))] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arrTrans[j][i] = arr[i][j]
    return arrTrans


def Del_Column(arr,a):
    delindex = set()
    for index, i in enumerate(arr):
        for index1, j in enumerate(i):
            if j == a:
                if index1 not in delindex:
                    delindex.add(index1)
    delindex = list(delindex)
    delindex.sort(reverse=True)
    arr = transp(arr)
    for i in delindex:
        del arr[i]
    arr = transp(arr)
    return print(arr)


matrix = [[9,2,5],[4,5,5],[7,8,9]]
Del_Column(matrix,5)