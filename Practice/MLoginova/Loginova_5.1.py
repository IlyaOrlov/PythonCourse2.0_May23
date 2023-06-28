#Реализовать алгоритм сортировки выбором
arr = [0, 3, 24, 2, 3, 7]
print(f"Массив до сортировки:\n{arr}")
i = 0
while i < len(arr)-1:
    m = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(f"Массив после сортировки:\n{arr}")
