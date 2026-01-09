from database import create_tables
from ui import welcome, action


def main():

    create_tables()

    account = welcome()

    action(account)


if __name__ == "__main__":
    main()