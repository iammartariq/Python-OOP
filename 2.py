class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, money):
        self.balance = self.balance - money
        print("Thankyou for your transaction!")
        print("Your remaining balance is: ", self.balance)

    def deposit(self, money):
        self.balance = self.balance + money
        print(self.balance)

    def getbalance(self):
        return self.balance
    
b1 = BankAccount(50000)
b1.withdraw(2500)
print(b1.getbalance())