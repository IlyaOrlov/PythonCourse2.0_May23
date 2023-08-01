# Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
# найти наименьший элемент в массиве
# поменять местами его и первый элемент в массиве
# найти следующий наименьший элемент в массиве
# и поменять местами его и второй элемент массива
# продолжать это пока весь массив не будет отсортирован
# arr = [0,3,24,2,3,7]
# // здесь реализованный алгоритм
# // на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]

def sort_arr(arr):
    for indx in range(len(arr)):
        ost_indx = indx + 1
        min_elem = arr[indx]
        for i in range(len(arr[ost_indx:])):
            if arr[ost_indx] < min_elem:
                min_elem = arr[ost_indx]
                arr[indx], arr[ost_indx] = arr[ost_indx], arr[indx]
            ost_indx +=1
    print(f'{arr}')
    return arr


arr = [0,3,24,2,3,7]


if __name__ == '__main__':
    sort_arr(arr)


