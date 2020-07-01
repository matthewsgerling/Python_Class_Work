import unittest
from Week10.StudentTest import Studentclass as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Gerling', 'Matt', 'programming', 3.9)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Gerling')
        self.assertEqual(self.student.first_name, 'Matt')
        self.assertEqual(self.student.major, 'programming')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Gerling')
        self.assertEqual(self.student.first_name, 'Matt')
        self.assertEqual(self.student.major, 'programming')
        self.assertEqual(self.student.gpa, 3.9)

    def test_student_str(self):
        self.assertTrue(self.student.__str__())

    def test_object_not_created_error_last_name(self):
        self.assertTrue(s.Student('Gerling'))

    def test_object_not_created_error_first_name(self):
        self.assertTrue(s.Student('Matt'))

    def test_object_not_created_error_major(self):
        self.assertTrue(s.Student('Gerling'))

    def test_object_not_created_error_gpa(self):
        self.assertTrue(s.Student('Gerling', 'Matt', 'programming'))


if __name__ == '__main__':
    unittest.main()
