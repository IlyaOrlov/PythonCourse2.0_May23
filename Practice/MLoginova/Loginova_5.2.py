#Написать и вызвать функцию, возвращающую первый повторившийся символ в переданном списке
def poisk(lst):
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] == lst[j]:
                return lst[i]


lst = list(input("Введите список: "))
#print(lst)
print(f"Первый повторившийся символ - это {poisk(lst)}")
