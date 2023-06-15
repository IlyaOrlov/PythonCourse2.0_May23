def minim(x):
    num_min = float("inf")
    idx_min = 0
    for index, i in enumerate(x):
        if i < num_min:
            num_min = i
            idx_min = index
    return num_min, idx_min


arr = [0, 54, 55, 53, 100, 51, 0, 8, 9, 0]


for index, _ in enumerate(arr):
    num_min, idx = minim(arr[index:])
    if idx:
        arr[idx + index] = arr[index]
        arr[index] = num_min

print(arr)
