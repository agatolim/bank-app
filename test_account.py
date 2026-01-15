import pytest
from account import Account

@pytest.mark.parametrize(
    "account_type, amount, expected_checking, expected_savings",
    [
        ("checking", 100, 100, 0),
        ("savings", 100 , 0, 100),
    ])

def test_deposit_success(account_type, amount, expected_checking, expected_savings):
    account = Account("John", "Smith", "JSmith")
    assert account.deposit(account_type, amount) is True
    assert account.checking == expected_checking
    assert account.savings == expected_savings

@pytest.mark.parametrize(
    "account_type, amount",
    [
        ("checking", -1),
        ("savings", -1),
        ("checking", 0),
        ("savings", 0),
    ]
)

def test_deposit_invalid_amount(account_type,amount):
    account = Account("John", "Smith", "JSmith")
    assert account.deposit(account_type, amount) is False
    assert account.checking == 0
    assert account.savings == 0

@pytest.mark.parametrize(
    "account_type, amount",
    [
        ("investments", 50),
        ("retirement", 100),
        ("gold", 10),
        ("bonds", 200),
    ],
)

def test_deposit_invalid_account_type(account_type, amount):
    account = Account("John", "Smith", "JSmith")
    assert account.deposit(account_type, amount) is False
    assert account.checking == 0
    assert account.savings == 0


@pytest.mark.parametrize(
    "account_type, amount, expected_checking, expected_savings",
    [
        ("checking", 50, 50, 100),
        ("savings", 50, 100, 50),
    ]
)


def test_withdraw_success(account_type, amount, expected_checking, expected_savings):
    account = Account("John", "Smith", "JSmith", 100, 100)
    assert account.withdraw(account_type, amount) is True
    assert account.checking == expected_checking
    assert account.savings == expected_savings


@pytest.mark.parametrize(
    "account_type, amount",
    [
        ("checking", -1),
        ("savings", -1),
        ("checking", 0),
        ("savings", 0),
    ]
)

def test_withdraw_invalid_amount(account_type, amount):
    account = Account("John", "Smith", "JSmith", 100, 100)
    assert account.withdraw(account_type, amount) is False
    assert account.checking == 100
    assert account.savings == 100

@pytest.mark.parametrize(
    "account_type, amount",
    [
        ("checking", 500),
        ("savings", 700),
    ]
)

def test_withdraw_insufficient_funds(account_type, amount):
    account = Account("John", "Smith", "JSmith", 100, 100)
    assert account.withdraw(account_type, amount) is False
    assert account.checking == 100
    assert account.savings == 100

@pytest.mark.parametrize(
    "account_type, amount",
    [
        ("investments", 50),
        ("retirement", 50),
    ]
)

def test_withdraw_invalid_account_type(account_type, amount):
    account = Account("John", "Smith", "JSmith", 100, 100)
    assert account.withdraw(account_type, amount) is False
    assert account.checking == 100
    assert account.savings == 100
