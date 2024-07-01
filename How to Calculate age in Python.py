# How to Calculate age in Python

from datetime import date

dob = date(1988,4,7)
today = date.today()

age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print(age)
