
"""Group Leader:Ezepue Ebuka Emmanuel
    Mat No:COS/5521/2019
    Group No: 3
 """

# Top-down approach

# Top-level program

def main():
    # Define the initial balance
    balance = 0

    # Implement a simple menu system using a while loop
    while True:
        print("Welcome to the banking system.")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit(balance)
        elif choice == "2":
            withdraw(balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


# Functions for each banking operation

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposited {amount}. New balance is {balance}.")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print(f"Insufficient funds. Balance is {balance}.")
    else:
        balance -= amount
        print(f"Withdrew {amount}. New balance is {balance}.")

def check_balance(balance):
    print(f"Current balance is {balance}.")


# Call the main function to start the program
main()
