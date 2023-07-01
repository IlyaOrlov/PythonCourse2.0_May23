import datetime


def fun(d_1, d_2):
    d = d_1
    n = 0
    while d <= d_2:
        if d.weekday() < 5:
            n += 1
        d += datetime.timedelta(days=1)
    print(f'Количество рабочих дней в период с {d_1} по {d_2}: {n}')


data = []
j = 0
while j < 2 and (s_in := input('Введите дату в формате ГГГГ-ММ-ДД: ')):
    s = ''
    for i in s_in:
        if i.isdecimal():
            s += i
    if len(s) != 8:
        print('Некорректная дата! Возможно надо добавить "0" к числу/месяцу?')
        continue
    else:
        try:
            data.append(datetime.date.fromisoformat(s))
            j += 1
        except Exception as ex:
            print(f'Некорректно задана дата: {ex}')
            continue

fun(data[1], data[0]) if data[0] > data[1] else fun(data[0], data[1])
