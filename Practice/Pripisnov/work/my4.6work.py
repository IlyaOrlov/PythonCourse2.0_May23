def print_big(a, b):
    if a > b:
        print("Большее число:", a)
    else:
        print("Большее число:", b)


def return_big(a, b):
    if a > b:
        return a
    else:
        return b


x = 4
y = 8

print_big(x, y)

result = return_big(x, y)
print("Большее число по месту вызова:", result)
