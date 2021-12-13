#need to redo both write orders for .csv file config
import csv

def read_orders(filename, list):
    with open ('orders.csv', 'r') as file:
        csv_file = csv.DictReader(file) 
        for row in csv_file:
            print(row)

def write_orders(filename, list):
    with open('orders.csv', 'a') as new_orders:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        new_orders = csv.DictWriter(new_orders, fieldnames=fieldnames, delimiter= ',')
        new_orders.writeheader()
        for line in new_orders:
            new_orders.writerow(line)
                    

def read_products(filename, list):
    with open('products.txt', 'r') as products_txt:
        contents = products_txt.readlines()
        for line in contents:  
            list.append(line.strip())


def read_couriers(filename, list):
    with open('couriers.txt', 'r') as couriers_txt:
        contents = couriers_txt.readlines()
        for line in contents:  
            list.append(line.strip())

def save_products(filename: str, products: list[str]) -> None:
    with open("products.txt",'w') as couriers_txt:
        for product in products:
            couriers_txt.write(f"{product}\n")

def save_couriers(filename: str, couriers: list[str]) -> None:
    with open("couriers.txt",'w') as couriers_txt:
        for courier in couriers:
            couriers_txt.write(f"{courier}\n")