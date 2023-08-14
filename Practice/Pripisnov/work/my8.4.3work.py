import itertools


# Функция, генерирующая все возможные комбинации строки 'password':
def generate_combinations():
    word = 'password'
    combinations = itertools.combinations(word, 4)
    result = list(combinations)
    return result


# Пример использования функции
res = generate_combinations()
for combination in res:
    print(combination)
