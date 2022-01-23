import function
import DB_Functions
import AppMenu
import cowsay
from DB_Functions import Product_DB, Courier_DB, Orders_DB, Orders_Status_DB
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
                    DB_Functions.print_table(Product_DB) 
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe2()
                    AppMenu.products_menu()
                elif product_menu == 2: 
                    function.clear_screen()
                    DB_Functions.add_product()
                    AppMenu.products_menu()
                elif product_menu == 3:
                    function.clear_screen()
                    DB_Functions.update_product()
                    AppMenu.products_menu()
                elif product_menu == 4:
                    function.clear_screen()
                    DB_Functions.delete_database(Product_DB,'products')
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
                    DB_Functions.print_table(Courier_DB)
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe3()
                    AppMenu.couriers_menu()
                elif couriers_menu == 2:
                    function.clear_screen()
                    DB_Functions.add_courier()
                    AppMenu.couriers_menu()
                elif couriers_menu == 3:
                    function.clear_screen()
                    DB_Functions.update_couriers()
                    AppMenu.couriers_menu()
                elif couriers_menu == 4:
                    function.clear_screen()
                    DB_Functions.delete_database(Courier_DB,'couriers')
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
                    DB_Functions.print_table(Orders_DB)
                    input('>>>: ')
                    function.clear_screen()
                    AppMenu.cafe4()
                    AppMenu.orders_menu()
                elif orders_menu == 2:
                    function.clear_screen()
                    DB_Functions.add_order()
                    AppMenu.orders_menu()
                elif orders_menu == 3:
                    function.clear_screen()
                    DB_Functions.updateOS()
                    #DB_Functions.updateOSJoin() Still a WIP
                    AppMenu.orders_menu()
                elif orders_menu == 4:
                    function.clear_screen()
                    DB_Functions.update_orders()
                    AppMenu.orders_menu()
                elif orders_menu == 5:
                    function.clear_screen()
                    DB_Functions.delete_database(Orders_DB, 'orders') 
                    AppMenu.orders_menu()
                    
        else:
            function.clear_screen
            cowsay.pig(Fore.RED +'Warning Input is not recognised')
            AppMenu.main_menu
            break
    except ValueError as e:
        function.clear_screen
        print(Fore.RED+'----------''\n''Please enter the correct input')




