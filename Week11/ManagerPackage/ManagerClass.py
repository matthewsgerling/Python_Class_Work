from Week11.PersonPackage.PersonClass import Person
from Week11.EmployeePackage.SalariedEmployee import SalariedEmployee as Employee


class Manager(Employee, Person):
    def __init__(self, fname, lname, dep):
        super().__init__(fname, lname)
        self.department = dep
        self.direct_reports: list = [Employee('John', 'Smith'), Employee('Logan', 'Ladwig'),
                                     Employee('Nate', 'Gerling')]

    def reports(self):
        print(self.direct_reports)


# Driver
ManagerMatt = Employee('Matt', 'Gerling', '7, 4, 2020', 40000)
ManagerMatt.display()  # Salaried Employee Display

ManagerMatt.give_raise(42000)
ManagerMatt.display()  # Salaried Employee Display

del ManagerMatt
