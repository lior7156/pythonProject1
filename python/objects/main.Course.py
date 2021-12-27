from python.objects.Course import Course

c_number=int(input("enter the course number: "))
c_name=input("enter the course name: ")
students_number=int(input("enter number of students: "))
max_students=int(input("enter max number of students: "))
c1=Course(c_number,c_name,students_number,max_students)
new_s=int(input("enter number of new students: "))
c1.new_students(new_s)

print(c1)