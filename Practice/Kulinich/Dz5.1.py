arr = [0,3,24,2,3,7]
def min(lst):
    a = float('inf')
    b = 0
    for index, value in enumerate(lst):
        if value < a:
            b = index
            a = value
    return b, a


i = 0
while i < len(arr):
    index, min_value = min(arr[i:])
    arr[index + i] = arr[i]
    arr[i] = min_value
    i += 1
print(arr) 