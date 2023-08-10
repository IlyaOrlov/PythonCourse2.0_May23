import datetime as dt


def string_as_date(str_as_date):
    return dt.datetime.strptime(str_as_date, "%d.%m.%Y").date()


def work_day(start_date, end_date_include, lst_holidays):
    start_date = string_as_date(start_date)
    end_date = string_as_date(end_date_include)
    new_holidays = [string_as_date(i) for i in lst_holidays]
    if end_date.weekday() > 4 or end_date in new_holidays:
        res = end_date - start_date
    else:
        res = end_date - start_date + dt.timedelta(days=1)
    while start_date != end_date:
        if start_date.weekday() > 4:
            res -= dt.timedelta(days=1)
        elif start_date in new_holidays:
            res -= dt.timedelta(days=1)
        start_date += dt.timedelta(days=1)
    return res


holidays = ("01.05.2023", "09.05.2023", "02.07.2023")
print(work_day("30.06.2023", "30.06.2023", holidays))
