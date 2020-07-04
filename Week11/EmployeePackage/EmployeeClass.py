class Employee:
    def __init__(self, fname, lname):
        self._firstName = fname
        self._lastName = lname

    def display(self):
        return self._firstName + ', ' + self._lastName
