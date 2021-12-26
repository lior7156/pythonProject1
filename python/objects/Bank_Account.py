class Bank_Account:
    def __init__(self,name,acc_number,balance):
        self.name=name
        self.acc_number=acc_number
        self.balance=balance

    def statement(self):
        """print account details"""
        print(f"name: {self.name}\n"
              f"account number:{self.acc_number}\n"
              f"balance:{self.balance}")

    def withdraw(self,amount):
        self.balance-=amount
        print(f"the balance after withdraw is:{self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"the balance after deposit is:{self.balance}")

my_account=Bank_Account("lior",134224,1000)
my_account.balance=10000
my_account.name="lior"
my_account.acc_number=134224
my_account.statement()
print()
your_account=Bank_Account("avi",1342550,5000)
your_account.balance=5000
your_account.name="avi"
your_account.acc_number=134550
your_account.statement()
your_account.withdraw(1000)
your_account.statement()