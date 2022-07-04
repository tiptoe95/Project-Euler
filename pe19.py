"""Counting Sundays"""
import datetime as dt
import calendar


day = dt.date(1901,1,1)
end_date = dt.date(2000,12,31)
wed_count = 0

while day != end_date:
    if day.weekday() == 6 and day.day == 1:
        print(day)
        wed_count += 1
    day += dt.timedelta(days=1)

print(wed_count)
