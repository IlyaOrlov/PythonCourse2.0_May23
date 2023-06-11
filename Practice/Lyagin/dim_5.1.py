
# def min_el(arr):
#     for i in range(len(arr)):
#         for k in range(i):
#             if arr[k] > arr[i]:
#                 arr[k],arr[i] = arr[i],arr[k]
#     return arr


arr = [0, 3, 24, 2, 3, 7]
# print(arr)
# print(min_el(arr))
j = 0
for i in range(len(arr)):
    if arr[i] <= arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        print(arr[i])
        print(arr)
j += 1
for i in range(j,len(arr)):
    if arr[i] <= arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        print(arr[i])
        print(arr)

j += 1
for i in range(j,len(arr)):
    if arr[i] <= arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        print(arr[i])
        print(arr)

j += 1
for i in range(j,len(arr)):
    if arr[i] <= arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        print(arr[i])
        print(arr)

j += 1
for i in range(j,len(arr)):
    if arr[i] <= arr[j]:
        arr[i],arr[j] = arr[j],arr[i]
        print(arr[i])
        print(arr)




