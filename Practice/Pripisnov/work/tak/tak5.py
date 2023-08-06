# Нужно реализовать итератор или генератор, который возвращает слова, начинающиеся с большой буквы
#class MyIter:
    #pass


def my_gen(s):
    i = 0
    while i < len(s)
        if s[i]
        yield i
        i += 1


s = "дорога дом Пётр компьютер Николай Алексей"

for i in my_gen(s):
    print(i)
