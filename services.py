from database import get_connection
from hashing import create_password
from account import Account

def update_balance(username, checking, savings):
    with get_connection() as conn:
        conn.execute("""
        UPDATE accounts 
        SET checking = ?, savings = ? 
        WHERE username = ?
        """, (checking, savings, username))
        conn.commit()



def create_account_db(first_name, last_name, username, password_hash, checking, savings):
    with get_connection() as conn:
        conn.execute('''
        INSERT INTO accounts (first_name, last_name, username, password_hash, checking, savings)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, username, password_hash, checking, savings))
        conn.commit()

def create_account(first_name, last_name, username, password):
    password_hash = create_password(password)
    create_account_db(first_name, last_name, username, password_hash, 0, 0)
    return Account(first_name, last_name, username, checking=0, savings=0)