# Changed formatting
# playing around with different potential approaches

import MyFunctions
#import pandas as pd
from MyFunctions import products, couriers, orders, order_status

try:
    MyFunctions.read_txt("products.txt", products)
    MyFunctions.read_txt("couriers.txt", couriers)
    #orders = pd.read_csv('orders.csv')
    MyFunctions.read_csv("orders.csv", orders)
except FileNotFoundError as f:
    print("Basic Load Files do not exist on the directory")


while True:
    try:
        Main_menu = ["---------", "Main Menu" '\n', "3 - Orders Menu", "2 - Couriers Menu", "1 - Show Products Menu", "0 - Exit & Save", "---------"]
        for main_items in Main_menu:
            print(main_items)
        main_menu = int(input('>>> '))
        if main_menu == 0:
            print("--------"'\n'"Application Terminated and Information saved"'\n'"--------"'\n')
            MyFunctions.save_txt('couriers.txt', couriers)
            MyFunctions.save_txt('products.txt', products)
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
            for menu in Products_menu:
                print(menu)
            while True:
                product_menu = int(input('>>> '))
                if product_menu == 0:
                        break
                elif product_menu == 1:
                    MyFunctions.txt_printer(products)
                elif product_menu == 2:
                    MyFunctions.create(products)
                elif product_menu == 3:
                    MyFunctions.update(products)
                elif product_menu == 4:
                    MyFunctions.delete(products)
    
        elif main_menu == 2:
            Couriers_menu = ["---------", 'Welcome to Couriers menu option:',"---------", '1 - List of couriers', '2 - Add a New Courier', '3 - Update an Existing Courier', '4 - Remove an Existing Courier', '0 - Exit to the Main Menu','---------']
            for c_items in Couriers_menu:
                print(c_items)
            while True:
                couriers_menu = int(input('>>> '))
                if couriers_menu == 0:
                        break
                elif couriers_menu == 1:
                    MyFunctions.txt_printer(couriers)
                elif couriers_menu == 2:
                    MyFunctions.create(couriers)
                elif couriers_menu == 3:
                    MyFunctions.update(couriers)
                elif couriers_menu == 4:
                    MyFunctions.delete(couriers)
    
        elif main_menu == 3:
            orders_menu = ["---------", 'Welcome to Orders Menu Option:',"---------", '1 - Orders Dictionary ', '2 - For Customers Information', '3 - Update an existing Order Status', '4 - Update an existing Order', '5 - Remove a courier', '0 - Exit to the Main Menu','---------']
            for order_items in orders_menu:
                print(order_items)
            while True:
                orders_menu = int(input('>>>'))
                if orders_menu == 0:
                        break
                elif orders_menu == 1:
                    MyFunctions.kwarg_printer(**orders)
                elif orders_menu == 2:
                    MyFunctions.csv_W3Custom_input(orders)
                    MyFunctions.dispatch(couriers)
                    print('ORDER STATUS = PREPARING')
                    orders['status']= 'PREPARING'
                    orders['orders']= '1'
                elif orders_menu == 3:
                    MyFunctions.get_user_inputW3(orders, order_status)
                elif orders_menu == 4:
                    MyFunctions.input_4W3(orders)
                elif orders_menu == 5:
                    MyFunctions.inputW3I5(orders)
                    
        else:
            print('Input is not recognised')
            break
    except ValueError as e:
        print('----------''\n''Please Enter The Correct Input''\n''------------''\n')




