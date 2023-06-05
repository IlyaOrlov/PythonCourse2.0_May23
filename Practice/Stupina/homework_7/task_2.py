def fun(lst):
    idx = []
    for idx_i, i in enumerate(lst):
        idx_i += 1
        idx += [(idx_j + idx_i) for idx_j, j in enumerate(lst[idx_i:]) if i == j]
    return lst[min(idx)]


lst = [4, 12, 1, 12, 3, 4]
print(f'Исходная строка: {lst} \nПервый повторившийся символ: {fun(lst)}')
