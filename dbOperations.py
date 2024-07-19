import sqlite3

database = "database.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to SQLite DB successful: {db_file}")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

def create_record(table, columns, values):
    conn = create_connection(database)
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in values])})"

    result = execute_query(conn, query, values)
    return result

def read_record(table, condition = None):
    conn = create_connection(database)
    query = f"SELECT * FROM {table}"
    if condition:
        query += f" WHERE {condition}"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
        return records
    except sqlite3.Error as e:
        print("Error reading records:", e)

def update_record(table, set_values, condition = None):
    conn = create_connection(database)
    query = f"UPDATE {table} SET {', '.join([f'{col} = %s' for col in set_values.keys()])} WHERE {condition}"
    values = list(set_values.values())
    execute_query(conn, query, values)

def delete_record(table, condition = None):
    conn = create_connection(database)
    query = f"DELETE FROM {table} WHERE {condition}"
    execute_query(conn, query)

def execute_query(conn, query, values=None):
    try:
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
        return True
    except sqlite3.Error as e:
        print("Error executing query:", e)
        return False

