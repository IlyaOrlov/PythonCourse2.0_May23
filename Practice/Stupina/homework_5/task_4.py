def fun_del(lst, x_del):

    for i, val in enumerate(lst):
        if x_del in val:
            count_del_col = 0
            for j in range(len(val)):
                if val[j - count_del_col] == x_del:
                    for n in lst:
                        del n[j - count_del_col]
                    count_del_col += 1
    return lst


matrix = [[1, 2, 2, 2], [4, 5, 6, 1], [2, 8, 9, 1]]
val_del = input(f'исходная матрица: {matrix} \nбудут удалены столбцы, содержащие число: ')
res = fun_del(matrix, int(val_del))
print(f'результат: {res}')
