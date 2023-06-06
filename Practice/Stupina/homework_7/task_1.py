def fun_min(lst):
    y = float('inf')
    y_index = float('-inf')
    for x, val in enumerate(lst):
        if y > val:
            y = val
            y_index = x
    return y, y_index


arr = [0, 1, 2, 3, 24, 2, 3, 7]
print(f'старая строка {arr}')

for i in range(len(arr)):
    j, j_index = fun_min(arr[i:])
    if j_index != 0:
        arr[j_index+i] = arr[i]
        arr[i] = j

print(f'новая строка {arr}')
