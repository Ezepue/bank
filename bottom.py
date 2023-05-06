
"""Group Leader:Ezepue Ebuka Emmanuel
    Mat No:COS/5521/2019
    Group No: 3
 """

# Bottom-up approach

# Functions for each banking operation

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposited {amount}. New balance is {balance}.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print(f"Insufficient funds. Balance is {balance}.")
    else:
        balance -= amount
        print(f"Withdrew {amount}. New balance is {balance}.")
    return balance

def check_balance(balance):
    print(f"Current balance is {balance}.")
    return balance


# Call the functions to perform the banking operations
balance = 0
balance = deposit(balance)
balance = withdraw(balance)
balance = check_balance(balance)
