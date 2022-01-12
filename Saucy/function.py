import csv
import os
from pyfiglet import Figlet
from colorama import init
from colorama import Fore, Back, Style
import loading_bars.loading_bars as bars

products = []
couriers = []
orders = []

order_status = ['CANCELLED', 'PREPARING', 'DISPATCHED', 'COMPLETED']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_csv(filename, csv_file):
    with open (filename, newline= '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_file.append(row)

def save_3csv(filename, list, fieldnames1, fieldnames2, f3):
    with open(filename, 'w') as csv_file:
        fieldnames = [fieldnames1, fieldnames2, f3]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter= ',')
        writer.writeheader()
        for row in list:
            writer.writerow(row)

def save_7csv(filename, list, f1, f2, f3, f4, f5, f6, f7): #can use ** KWARGS here
    with open(filename, 'w') as csv_file:
        fieldnames = [f1, f2, f3, f4, f5, f6, f7]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter= ',')
        writer.writeheader()
        for row in list:
            writer.writerow(row)

def p_printer(content):
    for row in content:
        print(row['name'],'-', row['price'])

def c_printer(content):
    for row in content:
        print(row['name'], '-', row['phone'])

def o_printer(content):
    for row in content:
        print(row['customer_name'], '-', row['customer_address'], '-', row['customer_phone'],'-', row['courier'],'-', row['status'], '/', row['items'])

def p_create(content):
    while True:
        try:
            product_name = input('Enter New Product Name: ')
            new_price = float(input('Enter New Product Price: '))
            new_product = {'name': product_name, 'price': new_price}
            content.append(new_product)
        except Exception as e:
            print("Error...Restarting")
        break

def c_create(content):
    while True:
        try:
            courier_name = input('Enter New Courier Name: ')
            new_number = input("Enter New Courier's Number: ")
            new_courier = {'name': courier_name, 'phone': new_number}
            content.append(new_courier)
        except Exception as e:
            print("Error...Restarting")
        break

def o_create(content, content2):
    while True:
        try:
            new_customer = input('Enter New Customer Name: ')
            new_address = input("Please Provide An Address: ")
            new_number = input("Enter New Customer's Number: ")

            print(list(enumerate(content2)))
            index = int(input("Select a Courier for dispatch: "))

            new_order = {'customer_name': new_customer, 
            'customer_phone': new_number, 
            'customer_address': new_address, 
            'courier': index, 
            'status': 'PREPARING', 
            'items': 'None'}
            content.append(new_order)
        except Exception as e:
            print("Error...Returning to Product Menu")
        break

def p_update(product_list):
    while True:
        try:
            for index, content in enumerate(product_list):
                print(index, content)
            list_index = int(input('Select option # >: '))
            product_to_update = product_list[list_index]

            print(product_to_update)

            name_product = str(input('Update the Name to: '))
            price_update = float(input('Update the Price to: '))
            product_list[list_index] = {'name': name_product, 'phone': price_update}
        except Exception as e:
            print("Error...Restarting")
        break

def c_update(courier_list):
    while True:
        try:
            for index, content in enumerate(courier_list):
                print(index, content)
            list_index = int(input('Select option # >: '))
            courier_to_update= courier_list[list_index]

            print(courier_to_update)

            name_update = str(input('Update the Name to: '))
            phone_update = str(input('Update the Phone # to: '))
            courier_list[list_index] = {'name': name_update, 'phone': phone_update}
        except Exception as e:
            print("Error...Restarting")
        break


def o_updateOS(orders_list, orders_status):
    while True:
        try:
            for index, content in enumerate(orders_list):
                print(index, content)
            list_index = int(input('Select option # to Update Order Status >: '))
            update_order_status = orders_list[list_index]

            print(update_order_status)

            print(list(enumerate(orders_status)))
            update_index = int(input('Update the ORDER STATUS using the option above: '))
            orders_list[list_index]['status'] = orders_status[update_index]
        except Exception as e:
            print("Error...Restarting")
        break

def delete(content):
    while True:
        try:
            print(list(enumerate(content)))
            delete = int(input('delete an order: '))
            del content[delete]
        except Exception as e:
            print("Error...Restarting")
        break

def dispatch(content):
    while True:    
        try:
            print(list(enumerate(content)))
            index = int(input("Select a Courier for dispatch: "))
            print(f'{content[index]} has been dispatched')
        except ValueError as e:
            print('Please enter the correct input from the list above')
        break

def o_update(orders_list, couriers, order_status):
    while True:
        for index, content in enumerate(orders_list):
            print(index, content)

        list_index = int(input('Select option # >: '))
        orders_to_update= orders_list[list_index]

        print(orders_to_update)
        cust_update = (input('Update the Name to: '))
        if cust_update == "":
            print('Cannot leave entry blank')
            break
        add_update = (input('Update the Address to: '))
        if add_update == "":
            print('Cannot leave entry blank')
            break
        phone_update = int(input('Update the Phone # to: '))
        if phone_update == "":
            print('Cannot leave entry blank')
            break
        print(list(enumerate(couriers)))
        courier_update = int(input('Update the Courier # to: '))
        if courier_update == "":
            print('Cannot leave entry blank')
            break
        print(list(enumerate(order_status)))
        status_update = int(input('Update the Order Status to: '))
        if status_update == "":
            print('Cannot leave entry blank')
            break
        items_update = (input('Update the items into: '))
        if items_update == "":
            print('Cannot leave entry blank')
            break

        orders_list[index] = {'customer_name': cust_update, 
        'customer_phone': phone_update, 
        'customer_address': add_update, 
        'courier': courier_update, 
        'status': order_status[status_update], 
        'items': items_update}
        break

