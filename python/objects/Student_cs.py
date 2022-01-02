class Student_cs:
    def __init__(self, id, name):
        if type(id) != int:
            raise TypeError("id must be of type int!!")
        if type(name) != str:
            raise TypeError("name must be of type str!!")

        self.id = id
        self.name = name
        self.subject_grades = {}

    def add_grade(self, subject, grade):
        if type(grade)!=int:
            raise TypeError("grade must be of type int!!")
        if grade<0 or grade>100:
            raise ValueError("grade must be between 0-100!!")
        self.subject_grades.update({subject: grade})

    def __str__(self):
        return f'id: {self.id}\nname: {self.name}\n' \
               f'subject and grades: {self.subject_grades}'

    def calc_factor(self, subject, factor):
        if type(factor)!=int:
            raise TypeError("factor must be of type int!!")
        if subject in self.subject_grades:
            factor = (factor*0.01)
            self.subject_grades[subject] += self.subject_grades[subject]*factor
            if self.subject_grades[subject]>100:
                self.subject_grades[subject]=100

    def average(self):
        sum = 0
        count = 0
        for grade in self.subject_grades:
            if grade in self.subject_grades:
                sum += grade
                count += 1
                average = sum / count
                return average

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

dan=Student_cs(12,'dan')
dan.subject_grades={'math': 90, 'english': 85, 'arabic': 80}
print(dan)
print(dan.average())