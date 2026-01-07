import sys
from database import create_tables
from ui import show_balance, get_user_info, deposit, withdraw
from auth import login
from services import update_balance, create_account

def main():

    create_tables()

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
                break
            else:
                print("Username or password is incorrect")

        elif status == "2":
            first_name, last_name, username, password = get_user_info()
            account = create_account(first_name, last_name, username, password)
            print("Sign up successful")
            break

        elif status == "3":
            print("Have a great day!")
            sys.exit()

        else:
            print("Invalid choice")



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



if __name__ == "__main__":
    main()