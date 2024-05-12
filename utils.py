import sqlite3


def get_tables(database='development.db'):
    ''' This function returns a list of all tables in the database. '''
    conn = sqlite3.connect(database)
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';"""
        )
        tables_names_list = [table[0] for table in cursor.fetchall()]
    return tables_names_list


def get_schema(database='development.db'):
    ''' This function returns a list of all tables in the database. '''
    conn = sqlite3.connect(database)
    schema = []
    with conn:
        for table in get_tables():
            cursor = conn.cursor()
            cursor.execute(f'PRAGMA table_info({table})')
            schema.append({table: {column[1]: column[2] for column in cursor.fetchall()}})
            cursor.close()
    return schema
