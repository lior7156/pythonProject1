from python.objects.Person import Person

# name=input("enter your name: ")
# age=int(input("enter your age: "))
# num_of_childrens=int(input("enter number of your children: "))
# person1=Person(name,age,num_of_childrens)
#
# person1.__str__()
# if person1.has_children():
#     print("the person has children")
# else:
#     print("the person has no children")
# person1.age_group()

p1=Person("dan",24,3)
p2=Person("dana",30,2)
p3=Person("ben",17,0)

list1=[p1,p2,p3]
print(list1)
print()
print(list1[2])