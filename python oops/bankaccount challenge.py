class minumumbalanceerror(Exception):
    pass
class bankaccount:
    account_number = 1001

    def __init__(self, name, balance):
        if balance < 1000:
            raise minumumbalanceerror("Account cant be created.")
        self.name = name
        self.balance = balance
        self.account_number = bankaccount.account_number
        bankaccount.account_number += 1


    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amt):
        if self.balance - amt < 1000:
            raise minumumbalanceerror("Amount can't be withdrawn.")
        else:
            self.balance -= amt
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

bal = bankaccount("Naman", 5000)
bal.deposit(100)
bal.withdraw(4000)
bal.show_details()
print("")
bal1 = bankaccount("Sohan", 1000)
bal1.show_details()