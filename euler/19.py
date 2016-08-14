import datetime

def find_number_of_sudays(start_date):
    enddate = datetime.date(2000, 12, 31)
    if start_date.weekday() != 6:
        current_day = start_date.weekday()
        additonal_day = 6 - current_day
        start_date = start_date + datetime.timedelta(days=additonal_day)

    count = 0
    while start_date < enddate:
        if start_date.day == 1:
            count+= 1
        start_date = start_date + datetime.timedelta(days=7)

    return count

date = datetime.date(1901, 01, 01)
print find_number_of_sudays(date)


from calendar import weekday
print sum(int(weekday(y, m, 1) == 6) for y in range(1901, 2001) for m in range(1, 13))

