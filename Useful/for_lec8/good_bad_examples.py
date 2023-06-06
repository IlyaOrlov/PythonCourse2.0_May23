# Антипример 1: не используйте глобальные переменные внутри функций
# def fun():
#     for i, _ in enumerate(lst):
#         lst[i] = lst[i] ** 2
#     return lst

# Антипример 2: не используйте объекты изменяемых типов данных в качестве значений по умолчанию
# def fun(lst=[1, 2, 3]):
#     for i, _ in enumerate(lst):
#         lst[i] = lst[i] ** 2
#     return lst

# Пример: задавайте значение по умолчанию правильно
def fun(lst=None):
    if lst is None:
        lst = [1, 2, 3]
    for i, _ in enumerate(lst):
        lst[i] = lst[i] ** 2
    return lst


lst = [1, 2, 3]
l1 = fun()
print(l1)
l2 = fun()
print(l2)
