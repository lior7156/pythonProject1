from python.objects.Student_cs import Student_cs

class Course_cs:
    def __init__(self,c_number, c_name, max_students):
        self.c_number=c_number
        self.c_name=c_name
        self.subject_teacher={}
        self.students_list=[]
        self.max_students=max_students

    def __str__(self):
        return f"course number: {self.c_number}\ncourse name: {self.c_name}" \
               f"\nmax of students number: {self.max_students}"

    def add_student(self,student):
        if self.students_list<self.max_students:
            student+=self.students_list
            print("the student is in the course now")
        else:
            print("there is not place left in the course,try again next time...")

    def add_factor(self,subject,factor):
        for i in self.students_list:
            i.calc_factor((subject,factor))

    def del_student(self,student):
        if student in self.students_list:
            self.students_list.remove(student)

    def averages(self):
        list_average_every_stu = []
        for i in self.students_list:
            list_average_every_stu.append(Student_cs.average(i))
        return list_average_every_stu

    def weak_students(self):
        lst_avg=self.averages()
        count=0
        lst_indexes=[]
        for i in lst_avg:
            if i==min(lst_avg):
                lst_indexes.append([i])
                count+=1
            else:
                count=1
        return lst_indexes,count



