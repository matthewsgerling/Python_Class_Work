from Week11.EmployeePackage.EmployeeClass import Employee
from _datetime import datetime


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, date, rate):
        super().__init__(fname, lname)
        self.startDate: datetime = date
        self.hourlyRate: float = rate

    def give_raise(self, rate):
        self.hourlyRate = rate

    def display(self):
        print(Employee.display(self), '\nHourly Rate:', self.hourlyRate, '\nStart Date:', self.startDate)


# Driver
Employee2 = HourlyEmployee('Matt', 'Gerling', '4, 4, 2020', 10.00)
Employee2.display()

Employee2.give_raise(14.00)
Employee2.display()

del Employee2
