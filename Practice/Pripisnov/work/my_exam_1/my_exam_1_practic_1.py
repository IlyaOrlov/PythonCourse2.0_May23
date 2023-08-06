def custom_len(lst):


    count = 0
    for _ in lst:
        count += 1
    return count

my_list = [1, 2, 3, 4, 5]
l = custom_len(my_list)
print(l)
