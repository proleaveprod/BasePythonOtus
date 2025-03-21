from colorama import Fore, init
from menu_content import *
init()

def start_message():
    message = (f"{Fore.GREEN}"
                "|============================|\n"
                "| Фига телефонный справочник |\n"
                "|============================|\n"
               f"{Fore.RESET}"
               )
    print(message)

def show_main_menu():
    for key,item in MAIN_MENU_ACTIONS.items():
        print(f"{key} - {Fore.MAGENTA}{item}{Fore.RESET}")

def get_choice(actions):
    while True:
        c = input(f'{Fore.LIGHTYELLOW_EX}Выбор:{Fore.RESET}')
        if c.isdigit():
            choice = int(c)
            if choice in actions:
                return choice
            else:
                print(f"{Fore.RED}Ошибка: {Fore.RESET}Нет такого действия")
        else:
            print(f"{Fore.RED}Ошибка: {Fore.RESET}Выберите номер действия")