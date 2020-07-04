from Week11.PersonPackage.PersonInheritance import Person


class Student(Person):
    def __init__(self, sid, fname, lname, m='Computer Programming', gpa='0.0'):
        super().__init__(lname, fname)
        self.major = m
        self.gpa = gpa
        self.student_id = sid

    def change_major(self, change):
        self.major = change

    def update_gpa(self, change):
        self.gpa = change

    def display(self):
        print(Person.display(self), 'Major:', self.major, '\nGpa:', self.gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', '4.0')
print(my_student.display())
del my_student
