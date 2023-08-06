# Написать и вызвать функцию, возвращающую первый повторившийся символ в переданном списке.
# Например, для  списка [2, 3, 4, 5, 3, 2] функция должна вернуть 3.

def compare_arg(arr):
    arr2 = set()
    for elem in arr:
        if elem in arr2:
            print(f'Первое повторяющееся число {elem}')
            return elem
        else:
            arr2.add(elem)


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 3, 2]
    compare_arg(arr)
