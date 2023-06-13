def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Пример функции:
arr = [0, 3, 24, 2, 3, 7]
sorted_arr = selection_sort(arr)
print(sorted_arr)
