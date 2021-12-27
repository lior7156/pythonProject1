from random import randint
class Lottery:
    def __init__(self):
        self.low=1
        self.up=45
        self.six_num_list=self.random_numbers_list()
        self.max_win=self.max_winning_number()

    def random_numbers_list(self):
        num=[randint(1,45) for i in range(6)]
        return num

    def max_winning_number(self):
        max_amount=int(input("enter max winning amount: "))
        return max_amount

    def print_random_number(self):
        print(self.random_numbers_list())

    def guess_number(self,number):
        if number in self.random_numbers_list():
            return True
        else:
            return False

    def amount_of_guesses(self,num):
        if num<=1:
            return 0
        elif 2<=num<=5:
            return (self.amount_of_guesses(num)*self.max_winning_number())/6
        elif num==6:
            return self.max_winning_number()

lottery1=Lottery()
lottery1.print_random_number()

for i in range(6):
    if 1<=i<=45:


    else:
        print("the user has been disqualified due to invalid guesses!")


