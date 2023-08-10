def minimal_lst(lst):
    a = float('inf')
    b = 0
    for index, value in enumerate(lst):
        if value < a:
            b = index
            a = value
    return b, a


arr = [0,3,24,2,3,7]
i = 0
while i < len(arr):
    index, min_value = minimal_lst(arr[i:])
    if index > 0:
        arr[index + i] = arr[i]
        arr[i] = min_value
    i += 1
print(arr) 