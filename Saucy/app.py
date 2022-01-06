import function
from function import products, couriers, orders, order_status

try:
    function.read_csv("products.csv", products)
    function.read_csv("couriers.csv", couriers)
    function.read_csv("orders.csv", orders)
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
            function.save_2csv('couriers.csv', couriers, 'name', 'phone' )
            function.save_2csv('products.csv', products, 'name', 'price')
            function.save_6csv('orders.csv', orders, 'customer_name', 'customer_address', 'customer_phone','courier', 'status', 'items')
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
                    function.p_printer(products)
                elif product_menu == 2:
                    function.p_create(products)
                elif product_menu == 3:
                    function.p_update(products)
                elif product_menu == 4:
                    function.delete(products)
    
        elif main_menu == 2:
            Couriers_menu = ["---------", 'Welcome to Couriers menu option:',"---------", '1 - List of couriers', '2 - Add a New Courier', '3 - Update an Existing Courier', '4 - Remove an Existing Courier', '0 - Exit to the Main Menu','---------']
            for c_items in Couriers_menu:
                print(c_items)
            while True:
                couriers_menu = int(input('>>> '))
                if couriers_menu == 0:
                        break
                elif couriers_menu == 1:
                    function.c_printer(couriers)
                elif couriers_menu == 2:
                    function.c_create(couriers)
                elif couriers_menu == 3:
                    function.c_update(couriers)
                elif couriers_menu == 4:
                    function.delete(couriers)
    
        elif main_menu == 3:
            orders_menu = ["---------", 'Welcome to Orders Menu Option:',"---------", '1 - Orders Dictionary ', '2 - For Customers Information', '3 - Update an Existing Order Status', '4 - Update an Existing Order', '5 - Remove a Order', '0 - Exit to the Main Menu','---------']
            for order_items in orders_menu:
                print(order_items)
            while True:
                orders_menu = int(input('>>> '))
                if orders_menu == 0:
                        break
                elif orders_menu == 1:
                    function.o_printer(orders)
                elif orders_menu == 2:
                    function.o_create(orders, couriers)
                elif orders_menu == 3:
                    function.o_updateOS(orders, order_status)
                elif orders_menu == 4:
                    function.o_update(orders, couriers, order_status)
                elif orders_menu == 5:
                    function.delete(orders)
                    
        else:
            print('Input is not recognised')
            break
    except ValueError as e:
        print('----------''\n''Please Enter The Correct Input''\n''------------''\n')




