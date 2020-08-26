import calendar

print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.leapdays(1990, 2020))
print()
print(calendar.month(2020, 8))
print(calendar.monthcalendar(2020, 8))
print()
print(calendar.calendar(2020))
is_leap = calendar.isleap(2021)
print(is_leap)
