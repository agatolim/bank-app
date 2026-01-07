class Account:
    def __init__(self, first_name, last_name, username, checking=0, savings=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.checking = checking
        self.savings = savings

    def deposit(self, account_type, amount):
        if amount <= 0:
            return False
        if account_type == "checking":
            self.checking += amount
        else:
            self.savings += amount
        return True

    def withdraw(self, account_type, amount):
        if amount <= 0:
            return False
        if account_type == "checking":
            if amount > self.checking:
                return False
            self.checking -= amount
        else:
            if amount > self.savings:
                return False
            self.savings -= amount
        return True