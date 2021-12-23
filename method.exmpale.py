# def מייצרת פונקציה של מה שאנחנו צריכים ומחזירה /
# לנו פלט במקרה שלנו ממוצע
def average(a,b):
    return (a+b)/2

num1=int(input("enter number: "))
num2=int(input("enter number: "))

avg = average(num1,num2)
print(avg)

# פונקציה שלוקחת את numbers משתי מספרים/
# ומחזירה סכום מכפלה חילוק והפרש
def numbers(a,b):
    sum=a+b
    diff=a-b
    mult=a*b
    div=a/b
    return [sum,diff,div,mult]

print(numbers(10,15))

























