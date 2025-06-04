'''
Create a class BankAccount where:
Each account has:
name (account holder's name)
balance

The interest rate is shared by all accounts (class variable).

There should be:
An instance method to display_account().
A class method to change_interest_rate(new_rate) which changes the interest rate for all accounts.
A method apply_interest() to add interest to that account's balance based on the current interest rate.
'''

class BankAccount:
    interest_rate = 1.5
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def display_account(self):
        print(f"name: {self.name}")
        print(f"balance: {self.balance}")
        print(f"balance: {self.balance * self.interest_rate}")
    
    @classmethod    
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        
    def apply_interest(self):
        print(f"new balance: {self.balance * self.interest_rate}")
        
a = BankAccount("Ritviz", 1000)
a.display_account()

BankAccount.change_interest_rate(2.0)

a.apply_interest()
    