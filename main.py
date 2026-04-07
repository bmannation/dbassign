import sqlite3


CREATE_DATA_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER)"
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?)"
GET_ALL_BEANS = "SELECT * FROM beans"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?"
GET_BEST_PREP = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect('data.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_DATA_TABLE)

def add_bean(name, method, rating):
    connection = connect()
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()
    
def sort_beans(connection, sort_by):
    if sort_by == "1":
        return connection.execute("SELECT * FROM beans ORDER BY name ASC").fetchall()
    elif sort_by == "2":
        return connection.execute("SELECT * FROM beans ORDER BY rating DESC").fetchall()
    elif sort_by == "3":
        return connection.execute("SELECT * FROM beans ORDER BY id ASC").fetchall()
    elif sort_by == "4":
        return connection.execute("SELECT * FROM beans").fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()
    
def get_best_prep(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREP, (name,)).fetchone()
    
def delete_bean(connection, name, bean_id):
    with connection:
        connection.execute("DELETE FROM beans WHERE name = ?", (name,))
        connection.execute("DELETE FROM beans WHERE id = ?", (bean_id,))