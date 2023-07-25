import copy


lst1 = [1, 2, 3, [4, [6, 8, [9, 100]]]]
# lst2 = [i for i in lst1]
lst2 = copy.deepcopy(lst1)
lst2[3][0] = 1000
print(lst1)
print(lst2)
