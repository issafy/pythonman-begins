import os
import colorama
from colorama import Back, Fore, Style

import service

colorama.init(autoreset=True)

data = [
    ['Name', 'Age', 'Country'],
    ['John', '25', 'USA'],
    ['Alice', '30', 'Canada'],
    ['Bob', '28', 'UK']
]
task_header = ['Name', 'Priority', 'Due Date', 'Complete']


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def __show_table__(table: list):
    table = [task_header, *table.copy()]
    # Determine the maximum width for each column
    column_widths = [max(len(item) for item in column) for column in zip(*table)]
    column_widths = [column_widths[0], 10, 20, 8]
    for x in range(len(table)):
        if x > 0:
            if table[x][3] == 'False':
                table[x][3] = f'{Back.LIGHTRED_EX} False {Back.LIGHTWHITE_EX} '
            elif table[x][3] == 'True':
                table[x][3] = f'{Back.LIGHTGREEN_EX} True {Back.LIGHTWHITE_EX}  '

    # Print the table with separators
    for i, row in enumerate(table):
        formatted_row = ' | '.join(item.ljust(width) for item, width in zip(row, column_widths))
        print(f'{Back.LIGHTWHITE_EX}{Fore.BLACK}| {formatted_row} |')
        if i == 0:
            separator = '+-' + '-+-'.join('-' * width for width in column_widths) + '-+'
            print(f'{Back.LIGHTWHITE_EX}{Fore.RED}{separator}')


def __show_item_0__():
    # clear_console()
    print(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}1-) Add task \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}2-) View Tasks \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}3-) Mark Task as Complete \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}4-) Close Console \n")


def __show_item_1__():
    clear_console()
    print(f"{Fore.LIGHTWHITE_EX}{Back.LIGHTGREEN_EX}1-) Add task \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}2-) View Tasks \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}3-) Mark Task as Complete \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}4-) Close Console \n")


def __show_item_2__():
    clear_console()
    print(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}1-) Add task \n")
    print(f"{Back.LIGHTGREEN_EX}{Fore.LIGHTWHITE_EX}2-) View Tasks \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}3-) Mark Task as Complete \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}4-) Close Console \n")


def __show_item_3__():
    clear_console()
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}1-) Add task \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}2-) View Tasks \n")
    print(f"{Fore.LIGHTWHITE_EX}{Back.LIGHTGREEN_EX}3-) Mark Task as Complete \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}4-) Close Console \n")


def __show_item_4__():
    clear_console()
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}1-) Add task \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}2-) View Tasks \n")
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}3-) Mark Task as Complete \n")
    print(f"{Fore.LIGHTWHITE_EX}{Back.LIGHTRED_EX}4-) Close Console \n")


def __start__():
    __show_item_0__()
    choice = input('What is your choice ?: ')
    if int(choice) == 1:
        __show_item_1__()
        confirm = input('\nConfirm ?(y/N): ')
        if confirm == 'yes' or confirm == 'y' or confirm == '':
            service.create_task()
            __start__()
        else:
            __start__()

    elif int(choice) == 2:
        if service.__task_count__() == 0:
            print(f'{Back.LIGHTRED_EX}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}There are currently no task here.')
            print(Back.RESET, Fore.RESET, Style.NORMAL)
        else:
            __show_table__(service.tasks.copy())
        __start__()

    elif int(choice) == 3:
        __show_item_3__()
        confirm = input('\nConfirm ?(y/N): ')
        if confirm == 'yes' or confirm == 'y' or confirm == '':
            service.__check_task__()
            __show_table__(service.tasks.copy())
            __start__()
        else:
            __start__()

    elif int(choice) == 4:
        __show_item_4__()
        confirm = input('\nAre you sure you want to leave ?(y/N): ')
        if confirm == 'yes' or confirm == 'y' or confirm == '':
            print(f"{Fore.RED}Exiting the application...{Style.RESET_ALL}")
        else:
            __start__()
