
def min_el(arr):
    for i in range(len(arr)):
        for k in range(i):
            if arr[k] > arr[i]:
                arr[k],arr[i] = arr[i],arr[k]
    return(arr)




arr = [0, 3, -8, 2, 3, 7]
print(arr)
print(min_el(arr))
