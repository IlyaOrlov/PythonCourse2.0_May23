def minmax(arr):
    n = len(arr)

    for i in range(n):
       # Находим наименьший элемент в оставшейся части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный наименьший элемент с текущим элементом

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



# Ввод массива пользователем
arr = input("Введите элементы массива, разделенные пробелом: ").split()
arr = [int(x) for x in arr]

# Сортировка массива с помощью алгоритма сортировки выбором
sorted_arr = minmax(arr)
print("Отсортированный массив:", sorted_arr)