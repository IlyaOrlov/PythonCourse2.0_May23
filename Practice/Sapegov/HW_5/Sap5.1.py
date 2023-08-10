def minimal(x):
    j = float('inf')
    n = 0
    for number, i in enumerate(x):
        if i < j:
            n = number
            j = i
    return n, j


lst = [0, 3, 24, 2, 3, 7]
y = 0
while y < len(lst):
    index, min_number = minimal(lst[y:])
    lst[index + y] = lst[y]
    lst[y] = min_number
    y += 1
print(lst)
