from datetime import datetime

# dates in string format
str_d1 = '2021/10/20'
str_d2 = '2022/2/20'

# convert string to date object
d1 = datetime.strptime(str_d1, "%Y/%m/%d").date()
d2 = datetime.strptime(str_d2, "%Y/%m/%d").date()

# difference between dates in timedelta
delta = d2 - d1
print(f'Difference is {delta.days} days')
