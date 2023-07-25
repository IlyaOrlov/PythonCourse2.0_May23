# Данная реализация просто демонстрирует последовательность рассуждений
# при создании алгоритмов. Приведённый ниже алгоритм не является правильным,
# так как работает не на всех наборах данных. Его еще отлаживать и отлаживать)

def minimum(arr):
    m = arr[0]
    i = 1
    while i < len(arr): # O(n)
        if m > arr[i]:
            m = arr[i]
        i += 1
    return m


lst = [3, 1, 2, 4]
i = 0
while i < len(lst):  # O(n)
    m = minimum(lst[i:])  # O(n)
    ind = lst.index(m)  # O(n)
    lst[i], lst[ind] = lst[ind], lst[i]
    i += 1
 # O(n) * (O(n) + O(n)) => O(n) * 2 * O(n)
print(lst)
