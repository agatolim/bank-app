import sys
from auth import duplicate_check, login
from services import create_account, update_balance

def welcome():
    print("************************")
    print("Welcome to the Bank of the People")
    print("************************")

    while True:
        status = input("1. Sign in\n2. Sign up\n3. Exit\nMake your choice(1, 2, 3): ")
        if status == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            account = login(username, password)
            if account:
                return account
            else:
                print("Username or password is incorrect")

        elif status == "2":
            first_name, last_name, username, password = get_user_info()
            account = create_account(first_name, last_name, username, password)
            print("Sign up successful")
            return account

        elif status == "3":
            print("Have a great day!")
            sys.exit()

        else:
            print("Invalid choice")

def action(account):
    while True:
        choice = input("What would you like to do today?\n1. Show Balance\n2. Deposit\n3. Withdraw\n4. Exit\nMake your choice(1, 2, 3, 4): ")

        if choice == "1":
            show_balance(account.checking, account.savings)

        elif choice == "2":
            print("************************")
            account_type = input("1. Checking Account\n2. Savings Account\nEnter your choice: ")
            print("************************")
            if account_type == "1":
                amount = deposit("checking")
                if amount > 0 and account.deposit("checking", amount):
                    update_balance(account.username, account.checking, account.savings)


            elif account_type == "2":
                amount = deposit("savings")
                if amount > 0 and account.deposit("savings", amount):
                    update_balance(account.username, account.checking, account.savings)

            else:
                print("Invalid choice")

        elif choice == "3":
            print("************************")
            account_type = input("1. Checking Account\n2. Savings Account\nEnter your choice: ")
            print("************************")
            if account_type == "1":
                amount = withdraw("checking", account.checking)
                if amount > 0 and account.withdraw("checking", amount):
                    update_balance(account.username, account.checking, account.savings)

            elif account_type == "2":
                amount = withdraw("savings", account.savings)
                if amount > 0 and account.withdraw("savings", amount):
                    update_balance(account.username, account.checking, account.savings)

            else:
                print("Invalid choice")

        elif choice == "4":
            print("************************")
            print(f"Checking Account Balance: ${account.checking:,.2f}\nSavings Account Balance: ${account.savings:,.2f}\nHave a nice day!")
            break
        else:
            print("That is not a valid choice")

    print(f"Thank you for using Bank of the People")
    print("************************")

def get_user_info():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    username = request_username()
    password = input("Please create your password: ").strip()
    return first_name, last_name, username, password


def deposit(account_type):
    try:
        print("************************")
        amount = input(f"Enter {account_type} deposit amount: $").strip()
        amount = float(amount)
        print("************************")
        if amount <= 0:
            print("That is not a valid amount")
            return 0
        else:
            return amount
    except (ValueError, TypeError):
        print("That is not a valid amount")
        return 0

def withdraw(account_type, balance):
    try:
        print("************************")
        amount = input(f"Enter {account_type} withdraw amount: $").strip()
        amount = float(amount)
        print("************************")
        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount <= 0:
            print("That is not a valid amount")
            return 0
        else:
            return amount
    except (ValueError, TypeError):
        print("That is not a valid amount")
        return 0

def show_balance(checking, savings):
    print("************************")
    print(f"Checking Account Balance: ${checking:,.2f}\nSavings Account Balance: ${savings:,.2f}")
    print("************************")


def request_username():
    while True:
        username = input("Please create your username: ").strip()
        if duplicate_check(username):
            print("Username already exists")
        else:
            return username