# datetime Class in Python

from datetime import datetime

dt1 = datetime(year = 2024 ,month = 6, day = 29)
dt2 = datetime(year = 2024 ,month = 6, day = 29,hour = 15 ,minute= 34)
dt3 = datetime(2018,5,26)
dt4 = datetime(2022,6,15,14,30)
print(dt1)
print(dt2)
print(dt3)
print(dt4)

print(dt1.year)
print(dt2.month)
print(dt3.day)
print(dt4.hour)

ct = datetime.now()
print(ct)
print(ct.day)
print(ct.hour)
print(ct.second)

ct1 = datetime.today()
print(ct1)
print(ct1.year)
print(ct1.second)
