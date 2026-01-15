import sqlite3

def get_connection(db_path="accounts.db"):
    return sqlite3.connect(db_path)

def create_tables():
    with get_connection() as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            first_name text not null,
            last_name text not null,
            username text PRIMARY KEY not null,
            password_hash BLOB not null,
            checking real default 0,
            savings real default 0
        )                   
        ''')
