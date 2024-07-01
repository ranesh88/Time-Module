# date class in Python

from datetime import date

d1 = date(year = 2024 , month= 6, day=29)
print(d1)

d2 = date(2024 , 6, 29)
print(d2)

print(d2.year)
print(d2.month)
print(d2.day)

cd = date.today()
print(cd)
print(cd.year)
print(cd.month)
print(cd.day)