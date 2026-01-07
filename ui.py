from auth import duplicate_check


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