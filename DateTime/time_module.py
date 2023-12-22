import datetime
from time import time, ctime, localtime

epoch = time()

print(epoch)

et = ctime(epoch)
print(et)

stobj = localtime()
print(stobj)
print("Hours",stobj.tm_hour)