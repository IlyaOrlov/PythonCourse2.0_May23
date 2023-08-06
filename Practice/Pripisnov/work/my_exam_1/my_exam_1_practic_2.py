def custom_reversed(lst):


    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


my_list = [1, 2, 3, 4, 5]
reversed_list = custom_reversed(my_list)
print(reversed_list)
