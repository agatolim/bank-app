from database import get_connection
from hashing import create_password
from account import Account

def update_balance(username, checking, savings, conn=None):
    if conn is None:
        conn = get_connection()
    with conn:
        conn.execute("""
        UPDATE accounts 
        SET checking = ?, savings = ? 
        WHERE username = ?
        """, (checking, savings, username))

def create_account_db(first_name, last_name, username, password_hash, checking, savings, conn=None):
    if conn is None:
        conn = get_connection()
    with conn:
        conn.execute('''
        INSERT INTO accounts (first_name, last_name, username, password_hash, checking, savings)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, username, password_hash, checking, savings))

def create_account(first_name, last_name, username, password, conn=None):
    password_hash = create_password(password)
    create_account_db(first_name, last_name, username, password_hash, 0, 0, conn)
    return Account(first_name, last_name, username, checking=0, savings=0)