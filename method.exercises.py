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

age=int(input("number: "))
while 0<=age<=120:
    while 0<=age<=18:
        print("child")
        age = int(input("number: "))
    while 19<=age<=60:
        print("adult")
        age = int(input("number: "))
    while 61<=age<=120:
        print("senior")
        age=int(input("number: "))
print("error")