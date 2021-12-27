class Course:
    def __init__(self,c_number,c_name,students_number,max_students):
        self.c_number=c_number
        self.c_name=c_name
        self.students_number=students_number
        self.max_students=max_students

    def __str__(self):
        return f"course number: {self.c_number}\ncourse name: {self.c_name}\n" \
               f"students number: {self.students_number}\n" \
               f"max number of students {self.max_students}"

    def course_place_number(self):
        place_number=self.max_students-self.students_number
        return place_number

    def new_students(self,new_s):
        if self.course_place_number()>=new_s:
            self.students_number+=new_s
        else:
            print("it is not possible to add more students!!")

