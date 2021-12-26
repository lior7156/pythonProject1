# *args=tuple כשאנחנו לא יודעים כמה פרמטרים יהיו לנו בפונקציה
# **kwargs=dictionary
def family_details(name,age,*children,**extra_details):
    print(f"name:{name}\nage:{age}")
    for i in children:
        print(i)
    for i in extra_details:
        print(f"{i}:{extra_details[i]}")

family_details("dan",30,children="gad and yaniv",phone="0523333333",
               address="yafo 57 tel aviv",email="abc@gmail.com")

print()
def family_details(name,age,salary=0,**kwargs):
    print(f"name:{name}\nage:{age}")
    print(f"salary:{salary}")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")

family_details("dani",24,3456,address="yafo 57 tel aviv")
