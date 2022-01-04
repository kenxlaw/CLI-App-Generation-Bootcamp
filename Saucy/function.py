import csv
#will change '[]' boxes on dictionary as new input turn into '[x]' but is functional.

products = []
couriers = []
orders = []

order_status = ['CANCELLED', 'PREPARING', 'DISPATCHED', 'COMPLETED']

products_dict = {'name': [], 'price': []}
couriers_dict = {'name': [], 'phone': []}
orders_dict = {'customer_name': [],'customer_address': [], 'customer_phone': [],'courier':[],'status': [], 'items': []}

def read_csv(filename, csv_file):
    with open (filename, newline= '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_file.append(row)

def save_2csv(filename, list, fieldnames1, fieldnames2):
    with open(filename, 'w') as csv_file:
        fieldnames = [fieldnames1, fieldnames2]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter= ',')
        writer.writeheader()
        for row in list:
            writer.writerow(row)

def save_6csv(filename, list, f1, f2, f3, f4, f5, f6):
    with open(filename, 'w') as csv_file:
        fieldnames = [f1, f2, f3, f4, f5, f6]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter= ',')
        writer.writeheader()
        for row in list:
            writer.writerow(row)

#def printer(content):
#      print(content)

def p_printer(content):
    for row in content:
        print(row['name'],'-', row['price'])

def c_printer(content):
    for row in content:
        print(row['name'], '-', row['phone'])

def o_printer(content):
    for row in content:
        print(row['customer_name'],'-', row['customer_address'], row['customer_phone'],'-', row['courier'],'-', row['status'], '/', row['items'])

def p_create(content):
    while True:
        new_product = input('Enter New Product Name: ')
        new_price = (input('Enter New Product Price: '))
        products_dict['name'].append(new_product)
        products_dict['price'].append(new_price)
        content.append(products_dict)
        break

def c_create(content):
    new_courier = input('Enter New Courier Name: ')
    new_number = input("Enter New Courier's Number: ")
    couriers_dict['name'].append(new_courier)
    couriers_dict['phone'].append(new_number)
    content.append(couriers_dict)

def p_update(content):
    for key,value in content:
        print(key, value)
        
    #get_index(content)
    #WIP

def delete(content):
    print(list(enumerate(content)))
    delete = int(input('delete an order: '))
    del content[delete]
    

def get_index(content):
    for content, index in enumerate(content):
        print(content, index)
    

def dispatch(content):
    while True:    
        try:
            print(list(enumerate(content)))
            index = int(input("Select a Courier for dispatch: "))
            print(f'{content[index]} has been dispatched')
        except ValueError as e:
            print('Please enter the correct input from the list above')
        break

def input3(content,content2):
    get_index(content)
    index = int(input('Select a number to UPDATE order Status: '))
    print(list(enumerate(content2)))
    update = int(input('Update the ORDER STATUS using the option above: '))
    content['status'] = content2[update]