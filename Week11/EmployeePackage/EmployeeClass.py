class Employee:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def display(self):
        print(self.firstName, ',', self.lastName)
