arr = [0,3,-8,2,3,7]


def min_el(arr):
    ind = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[ind]:
           ind = i
           arr[0], arr[ind] = arr[ind], arr[0]
print(arr)
min_el(arr)
print(arr)
