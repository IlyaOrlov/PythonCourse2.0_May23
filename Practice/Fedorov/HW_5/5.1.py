def minim(x):
    num_min = float("inf")
    for index, i in enumerate(x):
        if i < num_min:
            num_min = i
            idx_min = index
    return num_min, idx_min


arr = [0, 3, 24, 2, 3, 7]

for index, _ in enumerate(arr):
    num_min, idx = minim(arr[index:])
    arr[idx + index] = arr[index]
    arr[index] = num_min

print(arr)
