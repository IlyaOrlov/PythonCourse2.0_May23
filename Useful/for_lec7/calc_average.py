lst = []

while i := input("Введите что-нибудь: "):
    lst.append(i)

print(lst)
# найти среднее арифметическое чисел в списке lst

# ["abc", "123", "456"]

s = 0
n = 0
for i in lst:
    print(i)
    if i.isdigit():
        s += int(i)
        n += 1

print(s/n)



