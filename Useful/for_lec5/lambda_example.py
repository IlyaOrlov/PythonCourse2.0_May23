def check(x, y, compare):
    if compare(x, y):
        print(f"Выбираем {x}")
    else:
        print(f"Выбираем {y}")


# def get_min(a, b):
#     return a < b
#
#
# check(10, 20, get_min)
check(10, 20, lambda a, b: a < b)
check(10, 20, lambda a, b: a > b)