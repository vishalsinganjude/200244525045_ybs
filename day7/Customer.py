'''
1. Write python program to perform bank operations using class and objects.
Conditions:
    a. Bank name should be static.
    b. Using menu driven program.
1 .Deposit
2. Withdraw
3. Exit
'''

import sys
class Customer:
    bankName = "State Bank Of India"
    def __init__(self,name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("balance is : ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance please enter less amount than balance amount")
            sys.exit()
        self.balance -= amount
        print("Remaining balance is : ", self.balance)
print("Welcome to %s....How may I help U."%(Customer.bankName))
name = input("Plz Enter Your Name: ")
c = Customer(name)

while True:
    print("Enter Transaction:\n1.Withdraw\n2.Deposit\n3.Exit")
    option = int(input("Please Select an Option : "))
    if option == 1:
        amount = float(input("Enter Amount to withdraw : "))
        c.withdraw(amount)
    elif option == 2:
        amount = float(input("Enter Amount to Deposit in bank : "))
        c.deposit(amount)
    elif option == 3:
        print("Thank U, Visit Again !!!")
        break
    else:
        print("Invalid Option selection Plz try with another option.")
