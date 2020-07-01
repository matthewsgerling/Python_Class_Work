from _datetime import datetime


class EncapsulationAssignment:
    def __init__(self):
        self._firstName = "Matt"
        self._lastName = "Gerling"
        self._address = "123 Main Street, Urban, Iowa"
        self._phone_number = "515.555.5555 "
        self._salaried = True
        self._start_date = datetime(2019, 1, 1)
        self._salary = 40000

    def display(self, salaried):
        if salaried is False:
            return self._firstName + ', ' + self._lastName + '/n' + self._address + '/n' + self._start_date
        else:
            return self._firstName + ', ' + self._lastName + '/n' + self._address + '/n Annual Salary: ' + self._salary + self._start_date


print(EncapsulationAssignment())
