import datetime as dt

def date_as_string(date_as_str):
    return dt.datetime.strptime(date_as_str, "%d.%m.%Y").date()

def work_day(start_date, end_date, lst_holidays):
    start_date = date_as_string(start_date)
    end_date = date_as_string(end_date)
    new_holidays = []
    for i in lst_holidays:
        new_holidays.append(date_as_string(i))
    res = end_date - start_date + dt.timedelta(days=1)
    while start_date != end_date:
        if start_date.weekday() == 5 or start_date.weekday() == 6:
            res -= dt.timedelta(days=1)
        if start_date in new_holidays:
            res -= dt.timedelta(days=1)
        start_date += dt.timedelta(days=1)

    return res

holidays = ("01.05.2023","09.05.2023")
print(work_day("01.05.2023", "10.05.2023", holidays))



