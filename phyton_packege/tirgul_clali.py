# פייתון תרגילים בסיסי
# 1
# num1=int(input("enter number 1: "))
# num2=int(input("enter number 2: "))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)

# 2
# day = int(input("enter day: "))
# month = int(input("enter month: "))
# year = int(input("enter year: "))
#
# print(f"{day}/{month}/{year%100}")

# 3
num = int(input("enter 3 digit number: "))
print(f"{num%10}{num//10%10}{num//100}")

# 4
# name=input("enter name: ")
# year=int(input("enter year: "))
# age=int(input("enter age: "))
# future_year=int(input("enter future year: "))
#
# print(f"{name} will be {future_year-year+age} in year {future_year}")

#5
# num1=int(input("enter number: "))
# num2=int(input("enter number: "))
# num3=int(input("enter number: "))
#
# print(f"{num1}{num2}{num3}")
# print(f"{num1*2}{num2*2}{num3*2}")

# תרגילי תנאים
# 1
num1=int(input("enter number: "))
num2=int(input("enter number: "))
if num1+num2%2==0:
    print("double")
else:
    print("not double")

# 2

