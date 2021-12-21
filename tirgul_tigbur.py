# תרגיל 5 תרגילי תנאים
# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# if num1%2==0 and num2%2==0:
#     print(num1+num2)
# else:
#     print(num1*num2)
# תרגיל 1
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# if (a+b)%2==0:
#     print("even number")
# else:
#     print("odd number")
# תרגיל 3
# age=int(input("enter age: "))
# if 0<=age<=18:
#     print("child")
# elif 19<=age<=60:
#     print("adult")
# elif 61<=age<=120:
#     print("senior")
# elif age<0 or age>120:
#     print("invalid age")

# תרגילי לולאות בסיסיים
# תרגיל 10
# num=int(input("enter the number: "))
# count=0
#
# while num !=0:
#     num = int(input("enter the number: "))
#     if num%3==0 or num%7==0:
#         count+=1
# print(count)
# תרגיל 6
# grade=int(input("enter grades: "))
# count1=0
# count2=0
# sum1=0
# sum2=0
#
# while 0<=grade<=100:
#     if 60<=grade:
#         sum1+=grade
#         count1+=1
#     else:
#         sum2+=grade
#         count2+=1
#     grade = int(input("enter grades: "))
#
# print(sum1/count1)
# print(sum2/count2)

# תרגיל 2
# sum=0
# count=0
# for i in range(6):
#     num=int(input("enter number: "))
#     if num%2==0:
#         sum+=num
#         count+=1
# print(sum/count)

# תרגיל 3
# for i in range(10,100):
#     if i%10==7:
#         print(i,end=" ")

# תרגיל 4
# sum=0
# for i in range(10,100):
#     if i%10==0:
#         sum+=i
# print(sum)

# תרגיל 5
# grade=int(input("enter grades: "))
# sum=0
# count=0
# while 60<=grade<=100:
#     sum+=grade
#     count+=1
#     grade = int(input("enter grades: "))
# else: print("invalid grade!!")
# print("average: ",sum/count)

# תרגיל 7
# sum=0
# for i in range(5):
#     num=int(input("enter number: "))
#     sum+=num%10
# print(sum)

# תרגיל 8
# num=int(input("enter number: "))
# for i in range(1,num):
#     if i%5==0:
#         print(i,end=" ")

# תרגיל 9
# num=int(input("enter number: "))
# for i in range(2,num,2):
#     print(i,end=" ")