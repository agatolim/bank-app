import pytest
import sqlite3
from test_auth import temp_db
from services import update_balance, create_account_db, create_account
from hashing import create_password




def test_update_balance_success(temp_db):
    update_balance("JD", 500, 500, temp_db)

    cursor = temp_db.execute("SELECT checking, savings FROM accounts WHERE username = ?",
                   ("JD",))
    checking, savings = cursor.fetchone()

    assert checking == 500
    assert savings == 500

def test_update_balance_fail(temp_db):
    update_balance("NoUser", 500, 500, temp_db)

    cursor = temp_db.execute("SELECT checking, savings FROM accounts WHERE username = ?",
                   ("JD",))
    checking, savings = cursor.fetchone()

    assert checking == 100
    assert savings == 200

def test_create_account_db(temp_db):
    create_account_db("Jane", "Doe", "janedoe", create_password("secure456") , 1000, 1000, temp_db)

    cursor = temp_db.execute('''
        SELECT first_name, last_name, username, password_hash, checking, savings
        FROM accounts
        WHERE username = ?
        ''', ("janedoe",))

    account = cursor.fetchone()

    assert account["first_name"] == "Jane"
    assert account["last_name"] == "Doe"
    assert account["username"] == "janedoe"
    assert account["checking"] == 1000
    assert account["savings"] == 1000

def test_create_account_db_fail(temp_db):
    with pytest.raises(sqlite3.IntegrityError):
        create_account_db("Jane", "Doe", "JD", create_password("secure456"), 1000, 1000, temp_db)


def test_create_account(temp_db):
    account = create_account("Jane", "Doe", "janedoe", "secure456", temp_db)
    assert account.first_name == "Jane"
    assert account.last_name == "Doe"
    assert account.username == "janedoe"
    assert account.checking == 0
    assert account.savings == 0

def test_create_account_fail(temp_db):
    with pytest.raises(sqlite3.IntegrityError):
        create_account("Jane", "Doe", "JD", "secure456", temp_db)




