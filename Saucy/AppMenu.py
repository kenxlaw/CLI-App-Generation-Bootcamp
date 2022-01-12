import os
from pyfiglet import Figlet
from colorama import init
from colorama import Fore, Back, Style
from blessed import Terminal

init()


def cafe1():
    f = Figlet(font='thin')
    print (Fore.YELLOW + Style.DIM + f.renderText('** Saucey cafe **'))

def cafe2():
    f = Figlet(font='thin')
    print (Fore.BLUE + Style.DIM + f.renderText('~ Saucey cafe ~'))

def cafe3():
    f = Figlet(font='thin')
    print (Fore.GREEN + Style.DIM + f.renderText('# Saucey cafe #'))

def cafe4():
    f = Figlet(font='thin')
    print (Fore.RED + Style.DIM + f.renderText('$ Saucey cafe $'))

term = Terminal()

def main_menu():
    Main_menu = ["---------", 
                "Main Menu", 
                "---------" ,
                "3 - Orders Menu", 
                "2 - Couriers Menu", 
                "1 - Show Products Menu", 
                "0 - Exit & Save", 
                "---------"]
    for main_items in Main_menu:
        print(Fore.GREEN + main_items)

def products_menu():
    Products_menu = ["---------", 
                    'Welcome to Product Menu option:',
                    "---------",
                    '1 - Choice of Products', 
                    '2 - Create a New Product', 
                    '3 - Update an Existing Product', 
                    '4 - Delete an Existing Product', 
                    '0 - Exit to the Main Menu', 
                    "---------"]
    for menu in Products_menu:
        print(Fore.MAGENTA + menu)

def couriers_menu():
    Couriers_menu = ["---------", 
                    'Welcome to Couriers menu option:',
                    "---------", 
                    '1 - List of couriers', 
                    '2 - Add a New Courier', 
                    '3 - Update an Existing Courier', 
                    '4 - Remove an Existing Courier', 
                    '0 - Exit to the Main Menu',
                    '---------']
    for c_items in Couriers_menu:
        print(Fore.BLUE + c_items)

def orders_menu():
    orders_menu = ["---------", 
                'Welcome to Orders Menu Option:',
                "---------", 
                '1 - Orders Table', 
                '2 - Create Customers Information', 
                '3 - Update an Existing Order Status', 
                '4 - Update an Existing Order', 
                '5 - Remove a Order', 
                '0 - Exit to the Main Menu',
                '---------']
    for order_items in orders_menu:
        print(Fore.CYAN + order_items)