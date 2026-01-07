from account import Account
import hashing
from database import get_connection

def login(username, password):
    with get_connection() as conn:
        cursor = conn.execute("""
        SELECT first_name, last_name, username, password_hash, checking, savings
        FROM accounts
        WHERE username = ?
        """, (username,))

        row = cursor.fetchone()

        if row and hashing.check_password(password, row[3]):
            return Account(
                first_name = row[0],
                last_name = row[1],
                username = row[2],
                checking = row[4],
                savings = row[5]
            )
    return None


def duplicate_check(username):
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT 1 FROM accounts WHERE username = ?", (username,)
        )
        return cursor.fetchone() is not None
