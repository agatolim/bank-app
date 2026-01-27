from account import Account
import hashing
from database import get_connection
import logging

def login(username, password, conn=None):
    if conn is None:
        conn = get_connection()

    with conn:
        cursor = conn.execute("""
        SELECT first_name, last_name, username, password_hash, checking, savings
        FROM accounts
        WHERE username = ?
        """, (username,))

        row = cursor.fetchone()

        if row and hashing.check_password(password, row[3]):
            logging.info(f"User {username} logged in successfully")
            return Account(
                first_name = row[0],
                last_name = row[1],
                username = row[2],
                checking = row[4],
                savings = row[5]
            )
        else:
            logging.warning(f"Failed login attempt for user {username}")
    return None


def duplicate_check(username, conn=None):
    if conn is None:
        conn = get_connection()
    with conn:
        cursor = conn.execute(
            "SELECT 1 FROM accounts WHERE username = ?", (username,)
        )
        exists = cursor.fetchone() is not None
        if exists:
            logging.debug(f"Duplicate username check: {username} exists")
        return exists
