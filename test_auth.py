import sqlite3
import pytest
from hashing import create_password
from auth import login, duplicate_check


def init_db(conn):
    conn.execute('''
                CREATE TABLE accounts (
                    first_name text not null,
                    last_name text not null,
                    username text PRIMARY KEY not null,
                    password_hash BLOB not null,
                    checking real default 0,
                    savings real default 0
                )                   
                ''')


    accounts = ("John", "Doe", "JD", create_password("secure123"), 100, 200)
    conn.execute(
        "INSERT INTO accounts (first_name, last_name, username, password_hash, checking, savings)"
        "VALUES (?, ?, ?, ?, ?, ?)", accounts
    )
    conn.commit()

@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    init_db(conn)
    yield conn
    conn.close()

def test_login_success(temp_db):
    account = login("JD", "secure123", temp_db)
    assert account.first_name == "John"
    assert account.last_name == "Doe"
    assert account.username == "JD"
    assert account.checking == 100
    assert account.savings == 200

def test_login_failure(temp_db):
    assert login("JD", "wrongpassword", temp_db) is None


def test_duplicate_check_success(temp_db):
    assert duplicate_check("JD", temp_db) is True
    assert duplicate_check("Jdoe", temp_db) is False

