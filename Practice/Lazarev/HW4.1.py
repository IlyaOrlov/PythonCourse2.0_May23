# Я пытался вывести результат в строку, но не получилось
n = list(range(101))
m = []

for i in n:
    if i % 3 == 0:
        print('Fizz')
        m.append(i)
    elif i % 5 ==0:
        m.append(i)
        print('Buzz')
    elif i % 15 == 0:
        m.append(i)
        print('FizzBuzz')
    else:
        print(i)