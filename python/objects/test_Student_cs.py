from unittest import TestCase
from python.objects.Student_cs import Student_cs

class Test_Student_cs(TestCase):
    def setUp(self):
        print("set up")
        self.student1 = Student_cs(12,"lior")

    def test__init__1(self):
        # test a valid case of __init__
        self.assertEqual(self.student1.id,12)
        self.assertEqual(self.student1.name,"lior")

    def test__init__2(self):
        # test invalid parameters of __init__
        with self.assertRaises(TypeError):
            invalid_student=Student_cs("ab","lior")
        with self.assertRaises(TypeError):
            invalid_student=Student_cs(12,123)

    # test valid and invalid type of subject_grades
    def test__init__3(self):
        # valid
        self.assertEqual(self.student1.subject_grades, {})
        # invalid
        self.assertNotEqual(self.student1.subject_grades, [])

    def test_add_grade_1(self):
        # test valid add grade
        self.student1.add_grade('english',90)
        self.assertEqual(self.student1.subject_grades['english'],90)
        self.assertEqual(len(self.student1.subject_grades),1)

    def test_add_grade_2(self):
        # test invalid add grade
        with self.assertRaises(TypeError):
            self.student1.add_grade('english', 'aaa')
        with self.assertRaises(ValueError):
            self.student1.add_grade('english', 450)
        with self.assertRaises(ValueError):
            self.student1.add_grade('english', -45)

    def test_calc_factor__1(self):
        # test valid calc factor
        self.student1.add_grade('math' , 90)
        self.student1.calc_factor('math' , 10)
        self.assertEqual(self.student1.subject_grades['math'],99.0)

        # test valid calc factor gt 100
        self.student1.add_grade('math', 90)
        self.student1.calc_factor('math', 25)
        self.assertEqual(self.student1.subject_grades['math'], 100.0)


    def test_calc_factor__2(self):
        # test invalid calc factor as a string
        with self.assertRaises(TypeError):
            invalid_factor = self.student1.calc_factor(['english'], 'aaa')

        # test invalid float calc factor
        with self.assertRaises(TypeError):
            self.student1.add_grade('math', 80)
            self.student1.calc_factor('math', 10.5)
            self.assertEqual(self.student1.subject_grades['math'], 88.4)

    def test_average(self):
        # valid average test
        self.student1.subject_grades = {'math': 90, 'english': 85, 'arabic': 80}
        self.assertEqual(self.student1.average(), 85.0)

        # invalid type string grade
        with self.assertRaises(TypeError):
            self.student1.subject_grades = {'math': 90, 'english': 85, 'arabic': ''}
            self.student1.average()
            print(self.student1.average())

    def test__eq__(self):
        # valid test of __eq__
        self.dan=Student_cs(12,'dan')
        self.ben=Student_cs(12,'ben')
        self.assertEqual(self.ben,self.dan)

        # invalid test string id
        with self.assertRaises(TypeError):
            self.dan = Student_cs('aa', 'dan')
            self.ben = Student_cs(14, 'dan')

        # invalid test int name
        with self.assertRaises(TypeError):
            self.dan = Student_cs(12, 'dan')
            self.ben = Student_cs(12, 1345)
            self.assertEqual(self.ben, self.dan)



