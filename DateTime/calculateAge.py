from datetime import date

dob = date(year = 2000, month = 8, day = 31)
cd = date.today()
age_year = cd.year - dob.year
age_month = cd.month - dob.month
age_day = cd.day - dob.day
print((cd.month,cd.day) < (dob.month,dob.day))
print(age_year)