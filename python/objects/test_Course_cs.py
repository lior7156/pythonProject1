from unittest import TestCase
from python.objects.Course_cs_asi import Course_cs
from python.objects.Student_cs import Student_cs

class TestCourse_cs(TestCase):

    def setUp(self):
        print("setUp")
        self.course_Qa = Course_cs('Qa',15,50)
        self.student1 = Student_cs(12, 'lior')

    def test__init__1(self):
        # valid test of __init__
        self.assertEqual(self.course_Qa.c_name,'Qa')
        self.assertEqual(self.course_Qa.c_num,15)
        self.assertEqual(self.course_Qa.max_student_num,50)

    def test__init__2(self):
        # invalid test of __init__
        with self.assertRaises(TypeError):
            invalid_course=Course_cs(15,15,50)
        with self.assertRaises(TypeError):
            invalid_course=Course_cs('Qa','abc',50)
        with self.assertRaises(TypeError):
            invalid_course=Course_cs('Qa',15,'abc')
        with self.assertRaises(ValueError):
            invalid_course=Course_cs('Qa',15,-6)

    def test__init__3(self):
        # valid and invalid case of list and dictionary
        self.assertEqual(self.course_Qa.list_of_student_incourse,[])
        self.assertNotEqual(self.course_Qa.list_of_student_incourse,{})
        self.assertEqual(self.course_Qa.d1_subject_teacher,{})
        self.assertNotEqual(self.course_Qa.d1_subject_teacher,())

    def test_add_student1(self):
        # valid test of student add
        self.assertEqual(self.student1.id,12)
        self.assertEqual(self.student1.name,'lior')

    def test_add_student2(self):
        # invalid test of student add
        with self.assertRaises(TypeError):
            invalid_student = Student_cs('12','lior')
        with self.assertRaises(TypeError):
            invalid_student = Student_cs(12,67)

    def test_add_student3(self):
        self.c1 =Course_cs('Qa',15,3)
        self.s1 = Student_cs(11,'aaa')
        self.s2 = Student_cs(12,'bbb')
        self.s3 = Student_cs(13,'ccc')
        self.s4 = Student_cs(14,'ddd')
        self.c1.list_of_student_incourse.append(self.student1.name)
        self.assertEqual(self.c1.list_of_student_incourse,['lior'])
        self.assertTrue(len(self.c1.list_of_student_incourse)==1)
        self.c1.list_of_student_incourse.append(self.s2)
        self.c1.list_of_student_incourse.append(self.s3)
        print(len(self.c1.list_of_student_incourse))
        # self.c1.list_of_student_incourse.append(self.s4)
        # print(len(self.c1.list_of_student_incourse))


    def test_add_factor(self):
        self.student1.add_grade('math', 90)
        self.course_Qa.add_factor('math',10)
        self.assertEqual(self.student1.subject_grades['math'], 99.0)


    # def test_del_student(self):
    #     self.fail()
    #
    # def test_averages(self):
    #     self.fail()
    #
    # def test_weak_students(self):
    #     self.fail()
