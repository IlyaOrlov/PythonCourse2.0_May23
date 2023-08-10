import datetime


def delta(date0, date1):
    d = 0
    dif_date = date0
    while dif_date <= date1:
        if dif_date.weekday() < 5:
            d += 1
        dif_date += datetime.timedelta(days=1)
    return d


date0 = datetime.date(2023, 8, 1)
date1 = datetime.date(2023, 8, 31)
print(f'Количество рабочих дней: {delta(date0, date1)}')


