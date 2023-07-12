# Реализовать алгоритм сортировки от мин к макс
def mini(s):                # функц поиск минимального значения
    min_num = float('inf')  # минимальное значение почему-то +бесконечность?!
    min_idx = 0             # минимальный индекс
    for index, items in enumerate(s): # сотировака списка энумерэйт индекс, значение
        if items < min_num: # Если значение меньше минимального значение
            min_num = items # то минимальное значение = значению из списка
            min_idx = index # и его индекс = индексу минимального значения
    return min_idx, min_num # нишли и вернули мин значение и его индекс

def sort_min(x):                        # функция сортировки
    i = 0
    while i < len(x):
        min_idx, min_num = mini(x[i:])  # почему функц мини накидываем на срез?
        if min_idx != 0:
            x[i], x[min_idx + i] = x[min_idx + i], x[i] # какое i добавляется?
        i += 1
    return x


a = [0,3,24,2,3,7]
d = sort_min(a)
print(d)