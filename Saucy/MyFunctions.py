import csv

#Data Persistance

def read_txt(filename, list):
    with open(filename, 'r') as products_txt:
        contents = products_txt.readlines()
        for line in contents:  
            list.append(line.strip())

def save_txt(filename, list):
    with open(filename,'w') as object_txt:
        for line in list:
            object_txt.write(f"{line}\n")

# Data Encoding and Data Persistance

def csv_W3printer(filename, csv_reader):
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            print('Customer Name:', row['customer_name'],)
            print('Address: ', row['customer_address'])
            print('Phone:', row['customer_phone'])
            print('Courier Assigned:', row['courier'])
            print('Order Status: ', row['status'])

#Kinda broken, it saves but removes partial info, needs fixing.
def save_csv(filename, new_orders):
    with open(filename, 'w') as csv_file:
        headers = ['customer_name','customer_address','customer_phone','courier','status']
        new_orders = csv.DictWriter(csv_file, fieldnames=headers, delimiter= ',')
        new_orders.writeheader()

#def read_csv(filename, reader):
    #with open filename



#Functions for W1-3 utility

def txt_printer(contents):
    sContents = sorted(contents)
    print('---------')
    print('\n'.join(sContents),'\n''---------')


def delete(contents):
    while True:
        try:
            print(contents)
            del_input = input('Enter from the choice above that you wish to delete: ')
            contents.remove(del_input)
            print(contents)
            print(f'{del_input} has now been terminated.')
            break
        except ValueError as e:
            print('Please enter the correct input from the list above')
            break

def create(contents):
    new_content = (input("Enter new name: "))
    contents.append(new_content)
    print(contents)
    print(f'{new_content} has been added to the menu')

def update(contents):
    while True:    
        try:
            print(list(enumerate(contents)))
            index = int(input("Select a number for updating: "))
            item = (input("Enter a name for the updated input: "))
            contents[index] = item
            print(contents)
            print(f'{contents[index]} has been updated to the list above')
        except ValueError as e:
            print('Please enter the correct input from the list above')
        break

#functions for W3 Utilty

def csv_W3Custom_input(content):
    customer_name = input('Please provide a name: ')
    content['customer_name']= customer_name
    customer_address = input('Please provide an address: ')
    content['customer_address'] = customer_address
    customer_phone_number = int(input('Please provide a phone number: '))
    content['customer_phone_number'] = customer_phone_number
    save_csv('orders.csv', content)
    print('-----Dispatch option-----')

def dispatch(content):
    while True:    
        try:
            print(list(enumerate(content)))
            index = int(input("Select a Courier for dispatch: "))
            print(f'{content[index]} has been dispatched')
        except ValueError as e:
            print('Please enter the correct input from the list above')
        break

def append_dict(status):
    status['orders']= 'PREPARING'
    print("Order Status:", status['orders'])
