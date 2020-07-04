from Week11.EmployeePackage.EmployeeClass import Employee
from _datetime import datetime


class SalariedEmployee(Employee):
    def __init__(self, fname, lname, date, sal):
        super().__init__(fname, lname)
        self.startDate: datetime = date
        self.salary: int = sal

    def give_raise(self, sal):
        self.salary = sal

    def display(self):
        print(Employee.display(self), '\nSalary:', self.salary, '\nStart Date:', self.startDate)


# driver
Employee1 = SalariedEmployee('Matt', 'Gerling', '4, 4, 2020', 40000)
Employee1.display()
Employee1.give_raise(45000)
Employee1.display()

del Employee1
