def fun_min(lst):
    j = float('inf')
    for i, val in enumerate(lst):
        if j > val:
            j = val
            j_index = i
    return j, j_index


arr = [0, 3, 24, 2, 3, 7]
print(f'старая строка {arr}')

for i in range(len(arr)):
    j, j_index = fun_min(arr[i:])
    arr[j_index+i] = arr[i]
    arr[i] = j

print(f'новая строка {arr}')
