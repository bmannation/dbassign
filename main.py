import sqlite3


CREATE_DATA_TABLE = "CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER, sales INTEGER)"
INSERT_SALE = "INSERT INTO sales (name, method, rating, sales) VALUES (?, ?, ?, ?)"
GET_ALL_SALES = "SELECT * FROM sales"
GET_SALES_BY_NAME = "SELECT * FROM sales WHERE name = ?"
GET_BEST_PREP = """
SELECT * FROM sales
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect('data.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_DATA_TABLE)

def add_sale(name, method, rating, sales):
    connection = connect()
    with connection:
        connection.execute(INSERT_SALE, (name, method, rating, sales))

def get_all_sales(connection):
    with connection:
        return connection.execute(GET_ALL_SALES).fetchall()
    
def sort_sales(connection, sort_by):
    if sort_by == "1":
        return connection.execute("SELECT * FROM sales ORDER BY name ASC").fetchall()
    elif sort_by == "2":
        return connection.execute("SELECT * FROM sales ORDER BY rating DESC").fetchall()
    elif sort_by == "3":
        return connection.execute("SELECT * FROM sales ORDER BY id ASC").fetchall()
    elif sort_by == "4":
        return connection.execute("SELECT * FROM sales ORDER BY sales DESC").fetchall()
    elif sort_by == "5":
        return connection.execute("SELECT * FROM sales ORDER BY method ASC").fetchall()
    elif sort_by == "6":
        return connection.execute("SELECT * FROM sales").fetchall()

def get_sales_by_name(connection, name):
    with connection:
        return connection.execute(GET_SALES_BY_NAME, (name,)).fetchall()

def GET_SALES_BY_ID(connection, sale_id):
    with connection:
        return connection.execute("SELECT * FROM sales WHERE id = ?", (sale_id,)).fetchone()

def GET_SALES_BY_SALES(connection, sales):
    with connection:
        return connection.execute("SELECT * FROM sales WHERE sales = ?", (sales,)).fetchall()

def GET_SALES_BY_RATING(connection, rating):
    with connection:
        return connection.execute("SELECT * FROM sales WHERE rating = ?", (rating,)).fetchall()

def get_best_prep(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREP, (name,)).fetchone()
    
def delete_sale(connection, name, sale_id):
    with connection:
        connection.execute("DELETE FROM sales WHERE name = ?", (name,))
        connection.execute("DELETE FROM sales WHERE id = ?", (sale_id,))

def edit_sale(connection, sale_id, name, method, rating, sales):
    with connection:
        connection.execute("UPDATE sales SET name = ?, method = ?, rating = ?, sales = ? WHERE id = ?", (name, method, rating, sales, sale_id))