# найти минимальный элемент
lst = [4, -5, 1, 2, 3]
# 1
# i = min(lst)
# id = lst.index(i)
# print(id)

m = float('inf')
for i in lst:
    if i < m:
        m = i
print(m)



