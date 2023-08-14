# Написать функцию to_roman, которая принимает целое число, а возвращает строку, отображающую
# это число римскими цифрами. Например, на вход подается 6, возвращается - "VI";
# на вход подается 23, возвращается "XXIII". Входные данные должны быть в диапазоне от 1 до 5000,
# если подается число не из этого диапазона, или не число, то должны выбрасываться ошибка типа NonValidInput.
# Этот тип ошибки надо создать отдельно. Также необходимо в папке с файлом, содержащим вашу функцию,
# создать файл tests.py, внутри которой необходимо определить тесты для вашей функции.
# Тесты должны покрывать все возможное поведение функции, включая порождения ошибки при некорректных входных данных.
class NonValidInput(Exception):
    pass


def proccess_int(name):
    if not name.isnumeric() or int(name) not in range(0, 5001):
        raise NonValidInput()


def to_roman(x):
    dic = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI',
           '7': 'VII', '8': 'VIII', '9': 'IX'}
    s = ''
    try:
        proccess_int(x)
        for ind, i in enumerate(range(len(x), 0, -1)):
            raz = int(x[i-1])
            if ind == 0:
                s = dic[x[i-1]]
            elif ind == 1 or ind == 2:
                desyat = 'X' if ind == 1 else 'C'
                desyat1 = 'XL' if ind == 1 else 'CD'
                desyat2 = 'L' if ind == 1 else 'D'
                desyat3 = 'XC' if ind == 1 else 'CM'
                if raz < 4:
                    s = desyat * raz + s
                elif raz == 4:
                    s = desyat1 + s
                elif 4 < raz < 9:
                    s = desyat2 + desyat * (raz - 5) + s
                else:
                    s = desyat3 + s
            elif ind == 3:
                s = 'M' * raz + s

    except NonValidInput:
        print('Вы ввели не число, либо число вышло из диапазона')
    return s

if __name__ == '__main__':
    while (num := input('Введите число до 5000, либо stop: ')).lower() != 'stop':
        print(to_roman(num))
