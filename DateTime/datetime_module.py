from datetime import datetime, date,timedelta

# # creating date time object
# dt1 = datetime(year = 2019, month = 6, day= 30)
# print(dt1)

# # calling method using className

# ct = datetime.now()
# print("Today's date and time",ct)


# #printing current date
# cd = date.today()
# print("current date",cd)

# #time delta
# td = timedelta(days=100)
# today_date = date.today()
# print(today_date+td)

#date timeformatting

new_date = datetime.today()
print(new_date)

new_date1 = new_date.strftime("%B %d, %Y")
print(new_date1)

new_date2 = new_date.strftime("%H:%M:%S")
print(new_date2)

new_date3 = new_date.strftime("%b,%d,%Y")
print(new_date3)