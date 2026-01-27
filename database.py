import sqlite3

def get_connection(db_path="accounts.db"):
    return sqlite3.connect(db_path)

def create_tables():
    with get_connection() as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT PRIMARY KEY NOT null,
            password_hash BLOB NOT NULL,
            checking REAL DEFAULT 0,
            savings REAL DEFAULT 0
        )                   
        ''')
