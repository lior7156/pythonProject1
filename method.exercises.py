from random import randint
# 2 תרגיל
# def number(a):
#     if 100<=a<=999:
#         return True
#     else:
#         return False
#
# num = int(input("enter number: "))
# if number(num):
#     print("the number is 3 digits")
# else:
#     print("the number isn't 3 digits")

# תרגיל 1
# def _3_digit(a):
#     num1=a//100
#     num2=a//10%10
#     num3=a%10
#     return num1+num2+num3
# num=int(input("enter 3 digit number: "))
# print(_3_digit(num))

# תרגיל 3
# def name_number(a,b):
#     for i in range(b):
#         print(a)
#
# num1=input("enter name: ")
# num2=int(input("enter number: "))
# print(name_number(num1,num2))

# תרגיל 4
# def sum_of_number(a):
#     sum=0
#     for i in range(a+1):
#         sum+=i
#     return sum
#
# num1=int(input("enter number 1: "))
# print(sum_of_number(num1))

# תרגיל 5
# num2=int(input("enter number 2: "))
# print(sum_of_number(num2))
# num3=int(input("enter number 3: "))
# print(sum_of_number(num3))
# num4=int(input("enter number 4: "))
# print(sum_of_number(num4))
# num5=int(input("enter number 5: "))
# print(sum_of_number(num5))
# num6=int(input("enter number 6: "))
# print(sum_of_number(num6))

# תרגיל 6
# def print_2_numbers(a,b):
#     for i in range(a,b+1):
#         if a<=i<=b:
#             print(i,end=" ")
#     return
#
# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# print(print_2_numbers(num1,num2))

# תרגיל 7
# def maximum(a,b):
#     if a<b:
#         return b
# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# print(maximum(num1,num2))
#
# def minimum(a,b):
#     if a<b:
#         return a
# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# print(minimum(num1,num2))
# print(print_2_numbers(num1,num2))

# תרגיל 9
# def age_5_times(age):
#     for i in range(5):
#         while 0<=age<=120:
#             if 0<=age<=18:
#                 print("child")
#                 age = int(input("add your age: "))
#             elif 19<=age<=60:
#                 print("adult")
#                 age = int(input("add your age: "))
#             elif 61<=age<=120:
#                 print("senior")
#                 age = int(input("add your age: "))
#             else:
#                 print("invalid age!!")
#                 return i
#             break
# number = int(input("add your age: "))
# print(age_5_times(number))

# תרגיל 10
# def get_5_grades(a):
#     if 70<=a<=100:
#         return True
#     elif 0<=a<70:
#         return False
#
# for i in range(5):
#     num =int(input("enter grade: "))
#     if get_5_grades(num):
#         print("pass")
#     else:
#         print("fail")

# תרגיל 11
# def even_numbers(list1:list):
#     for i in range(2,41,2):
#         list1.append((i))

# list1=[]
# even_numbers(list1)
# print(list1)

# תרגיל 12
# def random_list(list1:list):
#     list1[:]=[randint(1,100) for i in range(20)]
    # for i in range(20):
    #     list1.append(randint(1,100))

# def count_num_in_list(num,list1:list):
#     return list1.count(num)

# list1=[]
# random_list(list1)
# print(list1)
# num=int(input("enter number: "))
# print(count_num_in_list(num,list1))

# # תרגיל 13
# def max_index(list1:list):
#     return list1.index(max(list1))

# print(max_index(list1))

# תרגיל 5 קובץ 2
# def convert_to_list(items):
#     if type(items) in [str,dict,tuple,set]:
#         list1=[i for i in items]
#         return list1
#     else:
#         print("invalid type")
#         return None
#
# print(convert_to_list((1,2,3,4,5)))
# print(convert_to_list({1,2,3,4,5}))
# print(convert_to_list(("abcd123")))
# print(convert_to_list({1:10,2:20,3:30,4:40}))
# print(convert_to_list(50))

# תרגיל 6
# def remove_from_list(list1:list,item):
#     item_location=list1.index(item)
#     list1[item_location:item_location+1]=[]
#     return list1
#
# list1=[1,2,3,4,5,4]
# remove_from_list(list1,4)
# print(list1)

# חוברת תרגילים תרגיל 10.1
# def tree_numbers(a,b,c):
#     return max(a,b,c)

# num1=int(input("enter number: "))
# num2=int(input("enter number: "))
# num3=int(input("enter number: "))
# print(tree_numbers(num1,num2,num3))

# 10.2
# def sum_list(list1:list):
#     list1[:]=[7,0,3,2,8]
#     for i in list1:
#         return sum(list1)
#
# list1=[]
# print(sum_list(list1))

# 10.3
# def mult_list():
#     list1=[7,-1,3,2,8]
#     mult=1
#     for i in list1:
#         mult*=i
#     return mult
#
# print(mult_list())

