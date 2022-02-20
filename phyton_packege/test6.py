# שאלה 3

#315
# number=int(input("315: "))
# print(number%10)
# print(number//10%10)
# print(number//100)
#
# print(f"{number%10}{number//10%10}{number//100}")

# try:
#     num= int(input("enter number: "))
# except:
#     print("error")
#     num=123
#     print(num)

def get_tree_numbers(num1,num2,num3):
    if num1>num2 and num1>num2:
        return num1
    elif num3>num2 and num3>num1:
        return num3
    elif num2>num3 and num2>num1:
        return num2

number1=int(input("enter number: "))
number2=int(input("enter number: "))
number3=int(input("enter number: "))
print(get_tree_numbers(number1,number2,number3))