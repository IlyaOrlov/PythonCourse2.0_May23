# написать и вызвать функцию, возвращающую первый повторившийся
# символ в переданном списке. Например, для  списка [2, 3, 4, 5, 3, 2] функция должна вернуть 3.
def povtor(x):
    new_list = set()
    for i in x:
        if i in new_list:
            return i
        new_list = list(new_list)
        new_list.append(i)


arr = [1, 3, 21, 4, 1, 3, 21, 1]
print(povtor(arr))
