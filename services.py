from database import get_connection
from hashing import create_password
from account import Account
import logging

def update_balance(username, checking, savings, conn=None):
    if conn is None:
        conn = get_connection()
    with conn:
        cursor = conn.execute("""
        UPDATE accounts 
        SET checking = ?, savings = ? 
        WHERE username = ?
        """, (checking, savings, username))

        if cursor.rowcount == 0:
            logging.warning(f"Attempted to update balance for a non-existent user {username}")
        else:
            logging.info(f"Updated balance for {username}: checking={checking}, savings={savings}")


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
    try:
        create_account_db(first_name, last_name, username, password_hash, 0, 0, conn)
        logging.info(f"Account {username} created successfully")
    except Exception as e:
        logging.error(f"Failed to create account {username}: {e}")
        raise
    return Account(first_name, last_name, username, checking=0, savings=0)