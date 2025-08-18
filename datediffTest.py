from datetime import datetime

d1 = str(input('Enter value 1: '))
d2 = str(input('Enter value2: '))
start = datetime.strptime(d1, "%H:%M:%S")
end = datetime.strptime(d2, "%H:%M:%S")

difference = end - start

seconds = difference.total_seconds()
print('difference in seconds is:', seconds)

minutes = seconds / 60
print('difference in minutes is:', minutes)

hours = seconds / (60 * 60)
print('difference in hours is:', hours)



