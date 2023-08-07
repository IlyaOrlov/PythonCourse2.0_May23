import datetime


def count_working_days(start_date, end_date):
    # Определяем список дней недели, считаемых рабочими
    working_days = [0, 1, 2, 3, 4]  # Понедельник (0) - Пятница (4)

    # Инициализируем счетчик рабочих дней
    count = 0

    # Перебираем каждый день между start_date и end_date
    current_date = start_date
    while current_date <= end_date:
        # Проверяем, является ли текущий день рабочим
        if current_date.weekday() in working_days:
            count += 1

        current_date += datetime.timedelta(days=1)

    return count


# Пример
start_d = datetime.date(2023, 1, 1)
end_d = datetime.date(2023, 1, 31)
working_d = count_working_days(start_d, end_d)
print("Количество рабочих дней:", working_d)
