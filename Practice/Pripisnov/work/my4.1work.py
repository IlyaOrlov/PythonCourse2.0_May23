a = "Fizz"
b = "Buzz"

for x in range (1,101):
    if x % (3*5) == 0:
        print(a+b)
    elif x % 3 == 0:
        print(a)
    elif x % 5 == 0:
        print(b)
    else:
        print(x)
    x += 1
