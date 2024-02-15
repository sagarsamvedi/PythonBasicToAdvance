from datetime import date

class Employee:
    def __init__(self, name, salary, company_name,date_of_joining):
        self.name = name
        self.salary = salary
        self.company_name = company_name
        self.date_of_joining = date_of_joining

    def getWorkingYears(self):
        today_date = date.today()
        return today_date.year - self.date_of_joining

e1 = Employee("sagar",100000,"volcanus",2021)
print(f"{e1.name} is working at {e1.company_name} for last {e1.getWorkingYears()} years")
    