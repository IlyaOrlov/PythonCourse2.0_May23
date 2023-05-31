# arr = [0,3,24,2,3,7]
# arr.sort()
# print(arr)
# Очень странно что не так :) Таков путь

arr = [0, 3, 24, 2, 3, 7]

for index, i in enumerate(arr):
    num_min = (min(arr[index::]))
    index_min = arr[index::].index(num_min) + index
    arr[index_min] = arr[index]
    arr[index] = num_min

print(arr)
