lst = (1, 2, 3, 4, 5)

# for i in lst:
#     print(i)

it = iter(lst)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

