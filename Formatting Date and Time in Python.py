# Formatting Date and Time in Python

from datetime import  datetime

dt =datetime.today()

print(dt)
print(type(dt))


newd1 = dt.strftime("%B%d,%Y")
print(newd1)


newd1 = dt.strftime("%d/%b/%Y")
print(newd1)


newd1 = dt.strftime("%d-%m-%Y")
print(newd1)


newd1 = dt.strftime("%H:%M:%S")
print(newd1)
print(type(newd1))