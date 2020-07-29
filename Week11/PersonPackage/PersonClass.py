
class Person:
    """Person class"""

    def __init__(self, lname, fname, add='Unknown'):
        self.last_name = lname
        self.first_name = fname
        self.address = add

    def display(self):
        print(self.last_name + ", " + self.first_name + " lives at " + self.address)
