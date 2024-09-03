import sqlite3
from sqlite3 import Error

def create_connection():
    path_db = 'data/ventas.db'

    try:
        connection = sqlite3.connect(path_db)
        return connection
    except sqlite3.Error as e:
        print(e)
        return None
    
def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_tables():
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        phone text NOT NULL,
                                        identity_card text NOT NULL
                                    ); """
    
    sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        stock integer NOT NULL,
                                        mensual_sales integer NOT NULL,
                                        installation integer NOT NULL,
                                        price integer NOT NULL
                                    ); """
    
    sql_create_employee_table = """ CREATE TABLE IF NOT EXISTS employees (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        phone text NOT NULL,
                                        password text NOT NULL
                                    ); """
    
    connection = create_connection()
    if connection is not None:
        create_table(connection, sql_create_users_table)
        create_table(connection, sql_create_products_table)
        create_table(connection, sql_create_employee_table)
    else:
        print("Error! No se pudo conectar a la base de datos")

def insert_user(User):
    sql = ''' INSERT INTO users(name,email,phone,identity_card)
              VALUES(?,?,?,?) '''
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(sql, User)
    connection.commit()
    return cur.lastrowid

def insert_product(Product):
    sql = ''' INSERT INTO products(name, stock, mensual_sales, installation, price)
              VALUES(?,?,?,?,?) '''
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(sql, Product)
    connection.commit()
    return cur.lastrowid

def insert_employee(Employee):
    sql = ''' INSERT INTO employees(name,email,phone,password)
              VALUES(?,?,?,?) '''
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(sql, Employee)
    connection.commit()
    return cur.lastrowid

def read_table(table):
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def read_table_by_condition(table, params, condition, value):
    connection = create_connection()
    cur = connection.cursor()
    
    cur.execute(f"SELECT {params} FROM {table} WHERE {condition} = ?", (value,))
    rows = cur.fetchall()
    return rows

def read_table_by_id(table, id):
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE id = {id}")
    rows = cur.fetchall()
    return rows

def update_table(table, id, data):
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(f"UPDATE {table} SET {data} WHERE id = {id}")
    connection.commit()

def delete_table(table, id):
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(f"DELETE FROM {table} WHERE id = {id}")
    connection.commit()