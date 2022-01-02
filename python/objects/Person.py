class Person:
    def __init__(self,id,name,age,num_of_childrens):
        self.id=id
        self.name=name
        self.age=age
        self.num_of_childrens = num_of_childrens

    def __repr__(self):
        """print  person details"""
        return f"\nid: {self.id}\nname: {self.name}\nage: {self.age}" \
               f"\nnumber of childrens: {self.num_of_childrens}"

    def has_children(self):
        if self.num_of_childrens >= 1:
            return True
        else:
            return False

    def age_group(self):
        if 0<=self.age<=18:
            print("child")
        elif 19<=self.age<=60:
            print("adult")
        elif 61<=self.age<=120:
            print("senior")

    def __eq__(self, other):
        if other is None:
            return False

        if type(other)!=Person:
            raise TypeError("invalid type: must compare two persons")

        if self.id==other.id and self.name==other.name:
            return True
        else:
            return False


