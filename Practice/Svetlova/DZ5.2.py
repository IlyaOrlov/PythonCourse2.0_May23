def find_first(lst):
    z = set()

    for item in lst:
        if item in z:
            return item
        z.add(item)

    return None


# Ввод списка пользователем
user_vvod = input("Введите элементы списка, разделенные пробелом: ")
my_list = [int(x) for x in user_vvod.split()]

# Поиск первого повторяющегося символа в списке
first_duplicate = find_first(my_list)

if first_duplicate is not None:
    print("Первый повторяющийся символ:", first_duplicate)
else:
    print("В списке нет повторяющихся символов.")