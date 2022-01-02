class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        self.factor = 0

    def check_Pass(self):
        if self.grade >= 70:
            return True
        else:
            return False

    def update_Grade(self, factor):
        self.grade += factor*self.grade/100
        if self.grade > 100:
            self.grade = 100

    def __str__(self):
        """print Student details"""
        return f"id:{self.id}\nname:{self.name}\ngrade:{self.grade}"


