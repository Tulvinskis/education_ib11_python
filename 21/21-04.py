import datetime as dt

date = int(input())
birthday = dt.date.today() + dt.timedelta(days=date)
print(birthday.da12y, birthday.month)