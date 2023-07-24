# Написать декоратор, выводящий "===========" до и после запуска функции.

def decor_fun(function_to_decorate):
    def inner_fun(*args, **kwargs):
        print('"==========="')
        res = function_to_decorate(*args, **kwargs)
        print('"==========="')
        return res
    return inner_fun

@decor_fun
def alone():
    print("Я просто функция, для проверки")


alone()
