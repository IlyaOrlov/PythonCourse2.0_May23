
# def min_el(arr):
#     for i in range(len(arr)):
#         for k in range(i):
#             if arr[k] > arr[i]:
#                 arr[k],arr[i] = arr[i],arr[k]
#     return arr



# print(arr)
# print(min_el(arr))


arr = [0, 3, 24, 2, 3, 7]

i = 0
while i < len(arr)-1:
    m = i
    j = i + 1

    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j = j+1
    if m != i:
        arr[i], arr[m] = arr[m], arr[i]
    i += 1

    print(arr)
