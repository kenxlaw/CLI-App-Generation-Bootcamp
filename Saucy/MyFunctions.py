import csv
#import pandas #....may be the way...

# very big band aid here for the rest of MP3 using (list(enumarate)) to show index for all options as opposed to specific.
# despite w3 spec saying print orders list with index, end result on terminal always looks clunky.
# Focused on one default order only, will probably need some kind of get_index function to resolve this.
# Running into an issue in trying to delete a dictionary key and value at the same time. (may be due to embeded dict?!?)
# Also loading .csv files through import function is a current nightmare.                          

#Data Persistance

products = []
couriers = []
orders = {
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2,
"status": "preparing"
}

order_status = ['CANCELLED', 'PREPARING', 'DISPATCHED', 'COMPLETED']

def read_txt(filename, list):
    with open(filename, 'r') as objects_txt:
        contents = objects_txt.readlines()
        for line in contents:  
            list.append(line.strip())

def save_txt(filename, list):
    with open(filename,'w') as object_txt:
        for line in list:
            object_txt.write(f"{line}\n")


def read_csv(filename, csv_file):
    with open (filename, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            list(row)



# Data Encoding and Data Persistance


def csv_load(filename, csv_reader):
    with open(filename, 'r') as file: 
        csv_reader = csv.DictReader(file, delimiter=',')
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
    print(f'{new_content} has been added to the list')

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
    #content['customer_name']= customer_name
    customer_address = input('Please provide an address: ')
    #content['customer_address'] = customer_address
    customer_phone_number = int(input('Please provide a phone number: '))
    #content['customer_phone_number'] = customer_phone_number
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


def get_user_inputW3(content,content2):
    print(list(enumerate(content)))
    index = int(input('Press 4 to UPDATE order Status: '))
    print(list(enumerate(content2)))
    update = int(input('Update the ORDER STATUS using the option above: '))
    content['status'] = content2[update]


def input_4W3(content):
    print(list(enumerate(content)))
    index =int(input('Choose which option you would like to update: '))
    if index == 0:
        print(content['customer_name'])
        update = input('Update customer name: ')
        content['customer_name'] = update
        print(content)
    elif index == 1:
        print(content['customer_address'])
        update = input('Update customer address: ')
        content['customer_address'] = update
        print(content)
    elif index == 2:
        print(content['customer_phone'])
        update = input('Update customer phone number: ')
        content['customer_phone'] = update
        print(content)
    elif index == 3:
        print(content['courier'])
        update = input('Update courier: ')
        content['courier'] = update
        print(content)
    elif index == 4:
        print(content['status'])
        update = input('update delivery status: ')
        content['status'] = update
        print(content)

def inputW3I5(content):
    print(content)
    orders = input("type 'delete' to remove order: ")
    if orders == 'delete':
        content['orders']= ''
    else:
        print('incorrect input')


def stretchW3I5(content):
    print(list(enumerate(content, start=-2)))
    update = input('Press 1 to delete a courier: ')
    print(content['courier'])
    delete = int(input('Type in the number of the courier you wish to delete: '))
    if delete <= 10:
        content['courier']= ''
    else:
        print('incorrect input')
    

#def append_dictI2(status):
#    status['orders']+= ['x']
#    print("Order Status:", status['orders'])

def kwarg_printer(**kwargs):
    for key, value in kwargs.items():
        print(key,': ',value)
#At some point I want to implement more Kwargs for better effiiency

def get_index(content):
    list.index(content)
