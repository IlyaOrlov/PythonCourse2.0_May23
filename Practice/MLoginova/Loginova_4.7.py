#Написать декоратор, выводящий "===========" до и после запуска функции.
def outer_fun(fun):
    def inner_fun(*args, **kwargs):
        const = "==========="
        print(const)
        res = fun(*args, **kwargs)
        print(const)
        return res
    return inner_fun


@outer_fun
def perimeter(x, y):
    result = 2 * (x+y)
    print(f"Периметр прямоугольника составляет {result} см.")
    return result


x = int(input("Введите ширину прямоугольника в см.: "))
y = int(input("Введите длину прямоугольника в см.: "))
perimeter(x, y)
