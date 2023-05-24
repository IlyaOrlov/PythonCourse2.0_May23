

# for x in range(1, 101):
#     if x % 15 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#          print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)
# Это первое , что пришло на ум.
# Но хочется что то более универсальное.
# По данным задачи вроде как просится, что если выполняется то и то, то и печатается то и то)
# Ниже вариант, что легко поменять и буквенные и числовые данные и вроде работает


str1 = "Fizz"
str2 = "Buzz"
y = 3
z = 5

for x in range(1, 101):
    if x % (y*z) == 0:
        print (str1+str2)
    elif x % y == 0:
        print(str1)
    elif x % z == 0:
         print(str2)
    else:
         print(x)
