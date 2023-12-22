from datetime import date,timedelta
import datetime
cd = date.today()

days = int(input("enter for how many next days you want the date :  "))
for i in range(1,days+1):
    td = datetime.timedelta(days= i)
    nextDay = cd+td
    print(f" next day is : {nextDay.day}-{nextDay.strftime('%B')} ")
