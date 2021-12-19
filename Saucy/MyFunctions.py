

#def read_csv(filename, file):
#    with open (filename, 'r') as file:
#        csv_file = csv.DictReader(file) 
#        for row in csv_file:
#            print(row)

#def save_csv(filename, file):
#    with open('orders.csv', 'w') as file:
#        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
#        new_orders = csv.DictWriter(, fieldnames=fieldnames, delimiter= ',')
#        new_orders.writeheader()
#        for line in new_orders:
#            new_orders.writerow(line)

# Menu printouts


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








#Functions for utility
#
def printer(contents):
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
            print(f'<{del_input}> has now been terminated.')
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
            print('Please enter the correct input from the list of products')
        break
