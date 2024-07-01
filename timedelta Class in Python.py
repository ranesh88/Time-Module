# timedelta Class in Python

from datetime import timedelta,date

td = timedelta(days=15)

print(td)

d = date.today()

print("Future date ::", d+td)
print("Previous date ::",d-td)
print("Current date ::",d)