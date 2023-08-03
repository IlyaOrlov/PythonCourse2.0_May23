import datetime

def count_working_days(start_date, end_date):
    days_count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            days_count += 1
        current_date += datetime.timedelta(days=1)

    return days_count

# Пример использования
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

working_days = count_working_days(start_date, end_date)
print("Количество рабочих дней:", working_days)