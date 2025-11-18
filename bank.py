class Bank:
    def __init__(self, accno, name, acctype, balance):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = int(balance)

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Amount deposited successfully.")
        print("Your current balance:", self.balance)

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
