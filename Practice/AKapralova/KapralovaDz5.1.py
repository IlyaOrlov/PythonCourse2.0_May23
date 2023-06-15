def fun_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[minimum], lst[i] = lst[i], lst[minimum]
    return lst


lst = [1, 3, 24, 2, 3, 7]
print(f"Исходный список: {lst}")
print(f"Отсортированый список: {fun_sort(lst)}")

# lst = [1, 3, 24, 2, 3, 7]
# lst.sort()
# print(lst)
