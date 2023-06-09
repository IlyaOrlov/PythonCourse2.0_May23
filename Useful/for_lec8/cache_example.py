from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


x = factorial(5)
print(x)

y = factorial(3)
print(y)

# 5! = 5 * 4! = 5 * 4 * 3!
