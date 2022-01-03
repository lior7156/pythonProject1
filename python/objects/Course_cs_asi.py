from Student_cs import Student_cs
class Course_cs:
    def __init__(self, c_name, c_num, max_stu_num):
        """defined each course has a name and number"""
        if type(c_name) != str:
            raise TypeError("course name must be str !!!")
        if type(c_num) != int:
            raise TypeError("course number must be str !!!")
        if type(max_stu_num) != int:
            raise TypeError("maximum student in the course must be str !!!")
        if max_stu_num<0:
            raise ValueError("course name must be str !!!")
        self.c_name = c_name
        self.c_num = c_num
        self.d1_subject_teacher = {}
        self.list_of_student_incourse = []
        self.max_student_num = max_stu_num



    def __repr__(self):
        return f"In the course: {self.c_name}, course number: {self.c_num} \n" \
               f"The subject-teacher list is: {self.d1_subject_teacher} \n" \
               f"The students list are: {self.list_of_student_incourse} \n" \
               f"maximum of student in the course: {self.max_student_num}"

    def add_student(self, id, name):
        """if there is room to student in the course, the method will add the student name to the list of this course student"""
        if type(id) != int:
            raise TypeError("id number must be int !!!")
        if type(name) != str:
            raise TypeError("name of student must be str !!!")
        student = Student_cs(id, name)
        if len(self.list_of_student_incourse) < self.max_student_num:
            self.list_of_student_incourse.append(student.name)
            return True
        else:
            return False

    def add_factor(self, subject, factor):
        if type(subject) != str:
            raise TypeError("subject must to be string!!!")
        if type(factor) != int:
            raise TypeError("factor must be int!!!")
        if factor<0:
            raise ValueError("factor must be above 0 !!!")
        if self.list_of_student_incourse == []:
            raise ValueError("you must have grades in your list")
        for i in self.list_of_student_incourse:
            i.calc_factor(subject,factor)

    def del_student(self, del_stu):
        for del_stu in self.list_of_student_incourse:
            self.list_of_student_incourse.remove(del_stu)

    def averages_course(self):
        """the method return a list of all the averages of the student in the course"""
        list_avg_every_stu = []
        for i in self.list_of_student_incourse:
            list_avg_every_stu.append(Student_cs.average(i))
        return list_avg_every_stu

    def week_student(self):
        """the method return the index of the weekes average grades"""
        lst_avg = self.averages_course()
        count = 0
        lst_indexes = []
        for i in lst_avg:
            if i == min(lst_avg):
                lst_indexes.append([i])
                count += 1
            else:
                count = 1
        return lst_indexes, count