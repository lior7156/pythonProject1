#שאלה 3
#num1=int(input("number 1:"))
#num2=int(input("number 2: "))
#while num1%2==0 and num2%2==0:
#    print(num1+num2)
#    num1 = int(input("number 1:"))
#    num2 = int(input("number 2: "))
#    print(num1*num2)

#שאלה 4
#num1=int(input("number 1:"))
#num2=int(input("number 2: "))
#while num1+num2==10:
#    num1 = int(input("number 1:"))
#    num2 = int(input("number 2: "))
#print("game over")

# שאלה 1
# num=int(input("enter 3 digit number: "))
# num1=num//100
# num2=num//10%10
# num3=num%10
# while 999>=num>=100:
#     print(num1+num2+num3)
#     num = int(input("enter 3 digit number: "))
# print("error")

# שאלה 2
# age=int(input("number: "))
# while 0<=age<=120:
#     while 0<=age<=18:
#         print("child")
#         age = int(input("number: "))
#     while 19<=age<=60:
#         print("adult")
#         age = int(input("number: "))
#     while 61<=age<=120:
#         print("senior")
#         age=int(input("number: "))
# print("error")

#שאלה 5
num=int(input("enter number: "))
while 100>num>9:
    while (num%7==0) and num>10: #מתחלקים ב7 בלי שארית
        print("luck")
        num = int(input("enter number: "))
# לולאה 2 מכניסה מספרים שהספרה הראשונה או השניה שלהם היא 7
    while ((num%10==7) or (num//10==7)) and num>=10:
        print("luck")
        num = int(input("enter number: "))
    num = int(input("enter number: "))
























