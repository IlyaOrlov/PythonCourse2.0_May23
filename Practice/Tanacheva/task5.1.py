# Алгоритм сортировки выбором
def find_min(lst):
    index, m = 0, lst[0]
    for i, j in enumerate(lst[1:]):
        if j < m:
            index, m = i + 1, j
    return index, m


def sort(lst):
    i = 0
    while i < len(lst):
        ind, m = find_min(lst[i:])  # поиск минимума
        if ind != 0:
            lst[i], lst[ind + i] = lst[ind + i], lst[i]
        i += 1
    return lst


lst = []
while j := (input("Введите список: ")):
    lst.append(int(j))

print(f"Отсортированный список: {sort(lst)}")
