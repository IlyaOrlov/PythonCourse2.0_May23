import datetime as dt


def string_as_date(str_as_date):
    return dt.datetime.strptime(str_as_date, "%d.%m.%Y").date()


def work_day(start_date, end_date_not_include, lst_holidays):
    start_date = string_as_date(start_date)
    end_date = string_as_date(end_date_not_include)
    new_holidays = []
    for i in lst_holidays:
        new_holidays.append(string_as_date(i))
    res = end_date - start_date
    while start_date != end_date:
        if start_date.weekday() > 4:
            res -= dt.timedelta(days=1)
        if start_date in new_holidays:
            res -= dt.timedelta(days=1)
        start_date += dt.timedelta(days=1)

    return res


holidays = ("01.05.2023", "09.05.2023")
print(work_day("30.06.2023", "03.07.2023", holidays))
