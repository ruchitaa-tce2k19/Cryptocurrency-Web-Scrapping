from datetime import datetime

# dates in string format
fromDate = (input("Enter from date in the format yyyy-mm-dd: "))
toDate = (input("Enter to date in the format yyyy-mm-dd: "))
str_d1 = '2021/10/20'
str_d2 = '2022/2/20'

# convert string to date object
d1 = datetime.strptime(fromDate, "%Y-%m-%d")
d2 = datetime.strptime(toDate, "%Y-%m-%d")

# difference between dates in timedelta
delta = d2 - d1
print(f'Difference is {delta.days} days')
noOfDays = delta.days
print(noOfDays)
