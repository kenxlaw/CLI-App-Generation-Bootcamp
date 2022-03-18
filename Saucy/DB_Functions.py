from logging import error, info
import dotenv
import pymysql
import os
import function
from pymysql.cursors import Cursor
from dotenv import load_dotenv
from prettytable import from_db_cursor
from colorama import init
from colorama import Fore, Back, Style
import loading_bars.loading_bars as bars


init()

DB_OS = 'orderid, status'
DB_Oindex = 'id, customer_name, status'

Product_DB = "SELECT id, name, price FROM products"
Courier_DB = "SELECT id, name, phone FROM couriers"
Orders_DB = "SELECT id, customer_name, customer_address, customer_phone, courier, status, items FROM orders"
Orders_Status_DB = "SELECT id, status FROM OrderStatus"

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


def add_product():
    while True:
        try:
            name = input('Enter New Product Name: ')
            price = input('Enter New Product Price: ')
            sql = f"INSERT INTO products (name, price) VALUES ('{name}','{price}')"

            execute_query(sql)

            bars.loading_info(info='Adding Product to Database Entry.')
            function.clear_screen()
            print(Fore.GREEN + f'{name} with a price of {price} has been added to the Database.')
        except Exception as e:
            function.clear_screen()
            bars.loading_info(info='Processing')
            print(Fore.RED + "Restarting. Error:" + str(e))
        break

def add_courier():
    while True:
        try:
            name = input('Enter New Courier Name: ')
            phone = input('Enter New Phone Number: ')
            sql = f"INSERT INTO couriers (name, phone) VALUES ('{name}','{phone}')"

            execute_query(sql)

            bars.loading_info(info='Adding New Courier to Database Entry.')
            function.clear_screen()
            print(Fore.GREEN + f'{name} with Phone # {phone} has been added to the Database.')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break


def update_product():
    while True:
        try:
            print_table(Product_DB)
            id_index = int(input('Enter id # to update from database: '))
            name = input('Enter New Product Name: ')
            price = input('Enter New Product Price: ')
            sql = (f"UPDATE products SET name = '{name}', price = '{price}' WHERE id={id_index}")
            execute_query(sql)

            id = input('Enter New ID: ')
            sql = (f"UPDATE products SET id = '{id}' WHERE id={id_index}")
            execute_query(sql)

            bars.loading_info(info='Updating Product to Database Entry.')
            function.clear_screen()
            print(Fore.GREEN + f'{name} with a price of {price} has been added to the Database, Entry ID {id}')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break

def update_couriers():
    while True:
        try:
            print_table(Courier_DB)
            id_index = int(input('Enter # to update from database: '))
            name = input('Enter New Courier Name: ')
            phone = input('Enter New Courier Phone #: ')
            sql = (f"UPDATE couriers SET name = '{name}', phone = '{phone}' WHERE id={id_index}")
            execute_query(sql)
            id = input('Enter New ID: ')
            sql = (f"UPDATE couriers SET id = '{id}' WHERE id={id_index}")
            execute_query(sql)
            bars.loading_info(info='Updating Couriers to Database Entry.')
            function.clear_screen()
            print(Fore.GREEN + f'{name} with phone # {phone} has been added to the Database, Entry ID # {id_index}')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break

def delete_database(schema, table):
    while True:
        try:
            print_table(schema)
            id_index = int(input('Enter id # to delete from database: '))
            sql = (f"DELETE FROM {table} WHERE id={id_index}")
            execute_query(sql)
            bars.dinamic_bar()
            function.clear_screen()
            print(Fore.RED + f'Entry ID #{id_index} has been removed from the Database.')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break

def add_order():
    while True:
        try:
            customer = input('Enter New Customer Name: ')
            address = input("Please Provide An Address: ")
            number = input("Enter New Customer's Number: ")
            print_table(Courier_DB)
            c_index = input('Enter a Courier id #: ')
            function.clear_screen()
            
            print_table(Product_DB)
            product = input('Enter a Product #: ')
            sql = f"INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) VALUES ('{customer}','{address}','{number}', '{c_index}','PREPARING', '{product}')"
            execute_query(sql)
            bars.loading_info(info='Adding Order to Database Entry')
            function.clear_screen()
            print(Fore.GREEN + f'{customer} at Address: {address} with Phone # {number} has been added to the Database.')
            print(Fore.GREEN + f"Order is set to'PREPARING' and has been allocated to Courier with ID #: {product}")
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break

def updateOS():
    while True:
        try:
            print_table(Orders_DB)
            id_index = int(input('Select Order #: '))
            function.clear_screen()
            print_table(Orders_Status_DB)
            order_status = input('Select Order Status # to Update: ')
            sql = (f"UPDATE orders SET status = {order_status} WHERE id={id_index}")
            execute_query(sql)
            bars.loading_info(info='Updating Update Order to Database Entry.')
            function.clear_screen()
            print(Fore.GREEN + f'For Order # {id_index}')
            print(Fore.GREEN + f'Order Status has been set to: {order_status}')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break
    
    

def updateOSJoin():
    print_table(Orders_DB)
    id_index = int(input('Select Order #: '))
    print_table(Orders_Status_DB)
    order_status = int(input('Select Order Status # to Update: '))
    sql= f"UPDATE orders SET status = orders.status = OrdersStatus.status[ {order_status}] FROM orders O INNER JOIN OrdersStatus OS on WHERE ID = {id_index};"
    execute_query(sql)


def update_orders():
    while True:
        try:
            print_table(Orders_DB)

            id_index = int(input('Select Order #: '))
            customer = input('Enter new customer name: ')
            address = input("Please provide an Address: ")
            number = input("Enter new customer's number: ")
            sql = (f"UPDATE orders SET customer_name = '{customer}', customer_address = '{address}', customer_phone = '{number}' WHERE id={id_index}")
            execute_query(sql)
            function.clear_screen()

            print_table(Product_DB)
            products = input('Select Product #: ')
            sql = (f"UPDATE orders SET items = '{products}' WHERE id={id_index}")
            execute_query(sql)
            function.clear_screen()

            print_table(Courier_DB)
            couriers = int(input('Select Courier id # to update to: '))
            sql = (f"UPDATE orders SET courier = '{couriers}' WHERE id={id_index}")
            execute_query(sql)
            bars.loading_info(info='Updating Couriers to Database Entry.')
            function.clear_screen()
            
            print(Fore.GREEN + 'Name set to:'f'{customer}')
            print(Fore.GREEN + 'Address set to: ' f'{address}')
            print(Fore.GREEN + 'Phone # set to: ' f'{number}')
            print(Fore.GREEN + 'Product ID set to: ' f'{products}')
            print(Fore.GREEN + 'Courier set to ID: ' f'{couriers}')
            print(Fore.LIGHTGREEN_EX + 'Succesfully Updated')
        except Exception as e:
            bars.loading_info(info='Processing')
            function.clear_screen()
            print(Fore.RED + "Restarting. Error:" + str(e))
        break


def print_table(schema):
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

    connection = pymysql.connect(host, user, password, database, autocommit=True)
    cursor = connection.cursor()
    cursor.execute(schema)
    mytable = from_db_cursor(cursor)
    print(mytable)
