# Finish rest of MP3 /finish DP for MP2
# Implement the save/load functions on MyFunction.py with this list without breaking other inputs. (touch up on data persistance)  

from input import couriers
from input import products
from input import orders



with open('couriers.txt', 'r') as reader:
    load_couriers = reader.read()

with open('products.txt', 'r') as reader:
    load_products = reader.readline()



while True:
    try:
        Main_menu = ["---------", "Main Menu" '\n', "3 - Orders Menu", "2 - Couriers Menu", "1 - Show Products Menu", "0 - Exit & Save", "---------"]
        for main_items in Main_menu:
            print(main_items)


        main_menu = int(input('>>> '))
        if main_menu == 0:
            print("--------"'\n'"Application Terminated and Information saved"'\n'"--------"'\n')
            try:
                file = open('couriers.txt', 'w')
                for person in couriers:
                    file.write(person + '\n')
            finally:
                file.close()

            try:
                file = open('products.txt', 'w')
                for product in products:
                    file.write(product + '\n')
            finally:
                    file.close()
            quit()
        elif main_menu == 1:
            print('Product Menu Option')
        elif main_menu == 2:
            print ("Couriers Menu Option")
        elif main_menu == 3:
            print ('Orders Menu Option')
        else:
            print('Input is not recognised')
            break

        if main_menu == 1:
            Products_menu = ["---------", 'Welcome to Product Menu option:',"---------",'1 - Choice of Products', '2 - Create a New Product', '3 - Update an Existing Product', '4 - Delete an Existing Product', '0 - Exit to the Main Menu', "---------"]
            for products_items in Products_menu:
                print(products_items)
            while True:
                product_menu = int(input('Enter a input for the Products Menu: '))
                if product_menu == 0:
                    break
                elif product_menu == 1:
                    print('---------')
                    print('\n'.join(products),'\n''---------')
                elif product_menu == 2:
                    new_product = (input("Enter new product name: "))
                    products.append(new_product)
                    print(products)
                    print(f'{new_product} has been added to the products menu')
                elif product_menu == 3:
                    while True:
                        try:
                            print(list(enumerate(products)))
                            index = int(input("Select the number corresponding to the product you would like to update: "))
                            item = (input("Enter the name of the new item: "))
                            products[index] = item
                            print(products)
                            print(f'^^^{products[index]} has been updated to the list above^^^')
                            break
                        except ValueError as e:
                            print('Please enter the correct input from the list of products')
                            break
                elif product_menu == 4:
                    while True:
                        try:
                            print(products)
                            del_input = input('Enter the name of the product you wish to delete: ')
                            products.remove(del_input)
                            print(products)
                            print(f'<{del_input}> has now been deleted from the products list.')
                            break
                        except ValueError as e:
                            print('Please enter the correct input from the list of products')
                            break
    
        elif main_menu == 2:
            Couriers_menu = ["---------", 'Welcome to Couriers menu option:',"---------", '1 - List of couriers', '2 - Add a New Courier', '3 - Update an Existing Courier', '4 - Remove an Existing Courier', '0 - Exit to the Main Menu','---------']
            for c_items in Couriers_menu:
                print(c_items)
            while True:
                couriers_menu = int(input('>>> '))
                if couriers_menu == 0:
                        break
                elif couriers_menu == 1:
                        couriers1 = sorted(couriers)
                        print('---------')
                        print('\n'.join(couriers1),'\n''---------')
                elif couriers_menu == 2:
                    new_courier = (input("Enter new courier name: "))
                    couriers.append(new_courier)
                    print(couriers)
                    print(f'{new_courier} has been added to the courier list')
                elif couriers_menu == 3:
                    while True:
                        try:
                            print(list(enumerate(couriers)))
                            index = int(input("Select the number corresponding to the courier you would like to update: "))
                            item = (input("Enter the name of the updated courier: "))
                            couriers[index] = item
                            print(couriers)
                            print(f'^^^{couriers[index]} has been updated to the list ^^^')
                            break
                        except ValueError as e:
                            print('Please enter the correct input from the list of couriers')
                            break
                elif couriers_menu == 4:
                    while True:
                        try:
                            print(couriers)
                            del_input = input('Enter the name of the courier you wish to remove: ')
                            couriers.remove(del_input)
                            print(couriers)
                            print(f'<{del_input}> has now been terminated.')
                            break
                        except ValueError as e:
                            print('Please enter the correct input from the list of couriers')
                            break
    
        elif main_menu == 3:
            orders_menu = ["---------", 'Welcome to Orders Menu Option:',"---------", '1 - Orders Dictionary ', '2 - For Customers Information', '3 - Update an existing Order Status', '4 - Update an existing Order', '5 - Remove a courier', '0 - Exit to the Main Menu','---------']
            for order_items in orders_menu:
                print(order_items)
            while True:
                orders_menu = int(input('>>>'))
                if orders_menu == 0:
                        break
                elif orders_menu == 1:
                    print(orders)
                elif orders_menu == 2:
                    print('Customer Name:', orders['customer_name'])
                    print('Address:', orders['customer_address'])
                    print('Phone Number:', orders['customer_phone'],'\n')
                    print('Choose a Courier')
                    print(list(enumerate(couriers)))
                    index = int(input("Select the number corresponding to the courier you would like to select: "))
                    print(f'You have chosen {couriers[index]} for dispatch')
                    #orders.append(order list)
                    print("Order Status: 'PREPARING'")
                    break
                elif orders_menu == 3:
                    #orders.append(orders)
                    print('TBC')
                elif orders_menu == 4:
                    print('update an existing order')
                elif orders_menu == 5:
                    while True:
                        try:
                            print(couriers)
                            del_input = input('Enter the name of the courier you wish to delete: ')
                            couriers.remove(del_input)
                            print(couriers)
                            print(f'<{del_input}> has now been deleted from the couriers list.')
                            break
                        except ValueError as e:
                            print('Please enter the correct input from the list of couriers')
                            break
                    break
        else:
            print('Input is not recognised')
            break
    except ValueError as e:
        print('----------''\n''Please Enter The Correct Input''\n''------------''\n')




