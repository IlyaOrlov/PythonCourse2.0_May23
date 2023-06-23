#Алгоритм сортировки выбором
def find_min(lst):
    m = lst[0]
    i = 1
    while i < len(lst):
        if m > lst[i]:
            m = lst[i]
        i += 1
    return m


def sort(lst):
    i = 0
    while i < len(lst):
        m = find_min(lst[i:])  # поиск минимума
        ind = lst.index(m, i)
        lst[i], lst[ind] = lst[ind], lst[i]
        i += 1
    return lst


lst = []
while j := input("Введите список: "):
    lst.append(j)

print(f"Отсортированный список: {sort(lst)}")
