def find_dup(lst1):
    lst2 = list()
    for i in lst1:
        if i in lst2:
            return i
        else:
            lst2.append(i)
    return None


lst = []
while j := input("Введите список: "):
    lst.append(j)

duplicate = find_dup(lst)
print(f"Первый повторившийся элемент в списке: {duplicate}")
