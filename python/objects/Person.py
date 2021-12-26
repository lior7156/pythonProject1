class Person:
    def __init__(self,name,age,num_of_childrens):
        self.name=name
        self.age=age
        self.num_of_childrens=num_of_childrens

    def age_group(self):
        if 0<=self.age<=18:
            return "child"
