def find_dup(lst1):
    lst2 = list()
    for i in lst1:
        if i in lst2:
            return i
        else:
            lst2.append(i)
    return None


def find_dup1(lst1):
    set1 = set()
    for i in lst1:
        if i in set1:
            return i
        set1.add(i)


lst = []
while j := input("Введите список: "):
    lst.append(j)

duplicate = find_dup1(lst)
print(f"Первый повторившийся элемент в списке: {duplicate}")
