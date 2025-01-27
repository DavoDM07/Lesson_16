#Dene a class named BankAccount with an __init__ method that initializes two
#instance variables: account_holder and balance.
#The class has methods like deposit and withdraw, each of which takes an amount as
#an argument and updates the account balance accordingly. These methods also
#include checks for valid input and available funds.
#The get_balance method allows you to retrieve the account balance.
#We create an Object of the BankAccount class called account1 with an initial balance
#of $1000.
#We deposit $500 and withdraw $200 from the account and print the account
#information.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.holder = account_holder
        self.balance = balance
    def deposit(self,money):
        try:
            money = int(money)
            if money <= 0:
                raise ValueError("Deposit is not positive ")
            self.balance += money
        except ValueError as error:
            print(f"Error {error}")
    def withdraw(self,money):
        try:
            money = int(money)
            if money > self.balance:
                raise ValueError("The allocated amount exceeds the amount on the balance")
            if money < 0:
                raise ValueError("Withdrawal funds must be positive")
            self.balance -= int(money)
        except ValueError as error:
            print(f"Error {error}")
    def get_balance(self):
        return self.balance
account1 = BankAccount("account1",1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())

