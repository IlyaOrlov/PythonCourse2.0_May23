def add(x,y):
    print(x+y)

def mydec(fun, *args):
    print("===========")
    fun(args[0],args[1])
    print("===========")

x = int(input("Введите 1ое число   "))
y = int(input("Введите 2ое число   "))
mydec(add,x,y)



