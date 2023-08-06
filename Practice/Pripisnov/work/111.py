arr = [0,3,24,2,3,7]
i = 0
while i < len(arr):
    m = min(arr[i:])
    ind =arr.index(m)
    arr[i], arr[ind] = arr[ind], arr[i]
    i += 1

print(m)
