def find_first_duplicate(lst):
    x = set()

    for i in lst:
        if i in x:
            return i
        x.add(i)

    return None


# Пример функции
my_list = [2, 3, 4, 5, 3, 2]
result = find_first_duplicate(my_list)
print("Первый повторяющийся символ:", result)
