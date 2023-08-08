import datetime


def fun_count(date1, date2):
    count = 0
    current_date = date1
    while current_date <= date2:
        if current_date.weekday() < 5:
            count += 1
        current_date += datetime.timedelta(days=1)
    return count


date1 = datetime.date(2018, 8, 21)
date2 = datetime.date(2023, 8, 3)
print(f"Количество рабочих дней: {fun_count(date1, date2)}")
