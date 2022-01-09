import dotenv
import pymysql
import os

from pymysql.cursors import Cursor
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
host,
user,
password,
database
)


def load_database(sql):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"SELECT * FROM {sql}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def execute_query(sql):
    try:
        connection = pymysql.connect(host, user, password, database, autocommit=True)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit
        cursor.close()
    finally:
        connection.close()
    return rows


def add_product(name,price):
    name = input('Enter New Product Name: ')
    price = input('Enter New Product Price: ')
    sql = f"INSERT INTO products (name, price) VALUES ('{name}','{price}')"
    execute_query(sql)

def add_courier(name,phone):
    name = input('Enter New Courier Name: ')
    phone = input('Enter New Phone Number: ')
    sql = f"INSERT INTO couriers (name, phone) VALUES ('{name}','{phone}')"
    execute_query(sql)

def update_product(content, table, id, name, price):
    load_database(content)
    id_index = int(input('Enter # to update from database: '))
    name = input('Enter New Product Name: ')
    price = input('Enter New Product Price: ')
    sql = (f"UPDATE {table} SET name = '{name}', price = '{price}' WHERE id={id_index}")
    execute_query(sql)
    id = input('Enter New ID: ')
    sql = (f"UPDATE {table} SET id = '{id}' WHERE id={id_index}")
    execute_query(sql)
    
def update_couriers(content, table, id, name, phone):
    load_database(content)
    id_index = int(input('Enter # to update from database: '))
    name = input('Enter New Courier Name: ')
    phone = input('Enter New Courier Phone #: ')
    sql = (f"UPDATE {table} SET name = '{name}', phone = '{phone}' WHERE id={id_index}")
    execute_query(sql)
    id = input('Enter New ID: ')
    sql = (f"UPDATE {table} SET id = '{id}' WHERE id={id_index}")
    execute_query(sql)

def delete_database(content, table):
    load_database(content)
    id_index = int(input('Enter # to delete from database: '))
    sql = (f"DELETE FROM {table} WHERE id={id_index}")
    execute_query(sql)

def add_order(content):
    new_customer = input('Enter New Customer Name: ')
    new_address = input("Please Provide An Address: ")
    new_number = input("Enter New Customer's Number: ")
    load_database(content)
# WIP
def updateOS(content):
    pass


