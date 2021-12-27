from python.objects.Student import Student

student1=Student(123,"lior",85)
if student1.check_Pass():
    print("passed")
else:
    print("failed")

factor=int(input("enter factor: "))
student1.update_Grade(factor)

student1.__str__()
print()
print(student1)
