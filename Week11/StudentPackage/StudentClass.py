from Week11.PersonPackage.PersonClass import Person

class Student:
    def __init__(self, m, gpa, person):
        self.major = m
        self.gpa = gpa
        self.Person = person

    def change_major(self, change):
        self.major = change

    def update_gpa(self, change):
        self.gpa = change

    def display(self):
        print('Person:', self.Person.display(), '\nMajor:', self.major, '\nGpa:', self.gpa)


p1 = Person('Matt', 'Gerling')
s1 = Student('Programming', '4.00', p1)
s1.display()

s1.change_major('Being Awesome')
s1.update_gpa('3.0')
s1.display()

