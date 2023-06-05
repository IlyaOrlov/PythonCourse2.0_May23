def fun_del(lst, x_del):

    for i in range(len(lst)):
        if x_del in lst[i]:
            count_del_col = 0
            for j in range(len(lst[i])):
                if lst[i][j - count_del_col] == x_del:
                    for n in range(len(lst)):
                        del lst[n][j - count_del_col]
                    count_del_col += 1
    return lst


matrix = [[1, 2, 2, 0], [4, 5, 6, 1], [1, 8, 9, 2]]
val_del = input(f'исходная матрица: {matrix} \nбудут удалены столбцы, содержащие число: ')
res = fun_del(matrix, int(val_del))
print(f'результат: {res}')
