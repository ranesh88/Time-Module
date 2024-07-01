# time Module in Python

from time import time, ctime, localtime
epoch = time()
print(epoch)

et = ctime(epoch)
print(et)

print(ctime())

stobj = localtime()

#print(stobj)

print("Year ::",stobj.tm_year)
print("Month ::",stobj.tm_mon)
print("Day ::",stobj.tm_mday)
print("Hour ::",stobj.tm_hour)
print("Minute ::",stobj.tm_min)
print("Second ::",stobj.tm_sec)

print("Indian Standard date format::")

print(stobj.tm_mday,end = '/')
print(stobj.tm_mon,end = '/')
print(stobj.tm_year)


print("Indian Standard time format::")

print(stobj.tm_hour, end = ':')
print(stobj.tm_min, end = ':')
print(stobj.tm_sec)




