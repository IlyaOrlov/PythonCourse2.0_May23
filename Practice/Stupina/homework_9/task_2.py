import datetime


def fun(d_1, d_2):
    i = 0
    while d_1 <= d_2:
        if d_1.weekday() < 5:
            i += 1
        d_1 += datetime.timedelta(days=1)
    return i


try:
    data_1 = input('Введите первую дату в формате год, месяц, число: ').split(',')
    data_2 = input('Введите вторую дату в формате год, месяц, число: ').split(',')
    data_1 = datetime.date(int(data_1[0]), int(data_1[1]), int(data_1[2]))
    data_2 = datetime.date(int(data_2[0]), int(data_2[1]), int(data_2[2]))
except Exception:
    print('Некорректно заданы даты')
else:
    if data_1 > data_2:
        res = fun(data_2, data_1)
        print(f'Количество рабочих дней в период с {data_2} по {data_1}: {res}')
    else:
        res = fun(data_1, data_2)
        print(f'Количество рабочих дней в период с {data_1} по {data_2}: {res}')
