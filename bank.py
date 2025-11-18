import random
class Bank:
    def __init__(self,name,acctype):
        self.accno = random.randint(1111111,9999999)
        self.name = name
        self.acctype = acctype
        self.balance = 0
        self.iscreated=True

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount<=0;

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")
            print("Current balance:", self.balance)


accno = int(input("Enter the account number: "))
name = input("Enter the name: ")
acctype = input("Enter the account type: ")
balance = int(input("Enter the current balance: "))

b = Bank(accno, name, acctype, balance)
b.deposit()
b.withdraw()
