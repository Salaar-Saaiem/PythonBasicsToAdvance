'''
4. Bank Account - Create a class BankAccount.

Attributes:
account_holder
balance

Methods:
deposit(amount)
withdraw(amount)
check_balance()

Example:
Deposited ₹500
Current Balance: ₹1500
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.acc_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited - {amount}')

    def withdraw(self, amount):
        self.balance -+ amount
        print(f'\nWithdrawn - {amount}')
    
    def check_balance(self):
        print(f'Current Balance - {self.balance}')


Saaiem=BankAccount('Saaiem', 500000)
Saaiem.deposit(50000)
Saaiem.check_balance()

