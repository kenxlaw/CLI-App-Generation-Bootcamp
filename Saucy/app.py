import function
import DB_Functions
import AppMenu
import cowsay
from DB_Functions import DB_product, DB_courier, DB_orders, DB_OS
from DB_Functions import DB_Pindex, DB_Cindex, DB_Oindex
from colorama import init
from colorama import Fore, Back, Style
import loading_bars.loading_bars as bars
from termcolor import colored

init()

bars.dinamic_bar()
bars.loading_info(info='Initialising the MiniProject')

print(colored('Presentation build #1', 'red', 'on_yellow'))

while True:
    try:
        AppMenu.cafe1()
        AppMenu.main_menu()
        main_menu = int(input('>>> '))
        if main_menu == 0:
            function.clear_screen()
            cowsay.cow("-"'\n'"Application Terminated. Information Saved. Moo!"'\n'"-"'\n')
            quit()
        elif main_menu == 1:
            function.clear_screen()
        elif main_menu == 2:
            function.clear_screen()
        elif main_menu == 3:
            function.clear_screen()
        else:
            function.clear_screen()
            print(Fore.RED + 'Input is not recognised')


        if main_menu == 1:
            AppMenu.cafe2()
            AppMenu.products_menu()
            while True:
                product_menu = int(input('>>> '))
                if product_menu == 0:
                    function.clear_screen()
                    break
                elif product_menu == 1:
                    bars.dinamic_bar()
                    function.clear_screen()
                    DB_Functions.print_table(DB_product,'products')
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe2()
                    AppMenu.products_menu()
                elif product_menu == 2:
                    function.clear_screen()
                    DB_Functions.add_product('name','price')
                    AppMenu.products_menu()
                elif product_menu == 3:
                    function.clear_screen()
                    DB_Functions.update_product(DB_product, 'products','id', 'name', 'price')
                    AppMenu.products_menu()
                elif product_menu == 4:
                    function.clear_screen()
                    DB_Functions.delete_database(DB_Pindex,'products', 'products')
                    AppMenu.products_menu()
    
        elif main_menu == 2:
            AppMenu.cafe3()
            AppMenu.couriers_menu()
            while True:
                couriers_menu = int(input('>>> '))
                if couriers_menu == 0:
                    function.clear_screen()
                    break
                elif couriers_menu == 1:
                    bars.dinamic_bar()
                    function.clear_screen()
                    DB_Functions.print_table(DB_courier,'couriers')
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe3()
                    AppMenu.couriers_menu()
                elif couriers_menu == 2:
                    function.clear_screen()
                    DB_Functions.add_courier('name','phone')
                    AppMenu.couriers_menu()
                elif couriers_menu == 3:
                    function.clear_screen()
                    DB_Functions.update_couriers(DB_courier,'couriers', 'id', 'name', 'phone')
                    AppMenu.couriers_menu()
                elif couriers_menu == 4:
                    function.clear_screen()
                    DB_Functions.delete_database(DB_Cindex, 'couriers', 'couriers')
                    AppMenu.couriers_menu()
    
        elif main_menu == 3:
            AppMenu.cafe4()
            AppMenu.orders_menu()
            while True:
                orders_menu = int(input('>>> '))
                if orders_menu == 0:
                    function.clear_screen()
                    break
                elif orders_menu == 1:
                    bars.dinamic_bar()
                    function.clear_screen()
                    DB_Functions.print_table(DB_orders,'orders')
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe4()
                    AppMenu.orders_menu()
                elif orders_menu == 2:
                    function.clear_screen()
                    DB_Functions.add_order(DB_courier, 'couriers', DB_product, 'products')
                    AppMenu.orders_menu()
                elif orders_menu == 3:
                    function.clear_screen()
                    DB_Functions.updateOS(DB_Oindex, 'orders', DB_OS, 'OrderStatus')
                    #DB_Functions.updateOSJoin('orders', 'OrderStatus')
                    AppMenu.orders_menu()
                elif orders_menu == 4:
                    function.clear_screen()
                    DB_Functions.update(DB_orders, 'orders',DB_product, 'products',DB_courier, 'couriers')
                    AppMenu.orders_menu()
                elif orders_menu == 5:
                    function.clear_screen()
                    DB_Functions.delete_database(DB_Oindex, 'orders', 'orders') 
                    AppMenu.orders_menu()
                    
        else:
            function.clear_screen
            cowsay.pig(Fore.RED +'Warning Input is not recognised')
            AppMenu.main_menu
            break
    except ValueError as e:
        function.clear_screen
        print(Fore.RED+'----------''\n''Please enter the correct input')




