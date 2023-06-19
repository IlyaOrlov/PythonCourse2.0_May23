def minimal(x):
    new_min = float("inf")
    n = 0
    for i, j in enumerate(x):
        if j < new_min:
            n = i
            new_min = j
    return n, new_min


arr = [0, 3, 24, 2, 3, 7]

a = 0
while a < len(arr):
    b, c = minimal(arr[a:])
    arr[b + a] = arr[a]
    arr[a] = c
    a += 1


print(arr)
