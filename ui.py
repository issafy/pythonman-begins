import os
import keyboard
import colorama
from colorama import Back, Fore
colorama.init(autoreset=True)

data = [
    ['Name', 'Age', 'Country'],
    ['John', '25', 'USA'],
    ['Alice', '30', 'Canada'],
    ['Bob', '28', 'UK']
]
task_header = ['Name', 'Priority', 'Due Date']


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def key_listener():
    def on_key_press(event):
        if event.name == '1':
            __show_item_1__()
        elif event.name == '2':
            __show_item_2__()
        elif event.name == '3':
            __show_item_3__()
        elif event.name == '4':
            __show_item_4__()

    keyboard.on_press(on_key_press)

    keyboard.wait('esc')


def __show_table__(table: list):
    table.insert(0, task_header)
    # Determine the maximum width for each column
    column_widths = [max(len(item) for item in column) for column in zip(*table)]

    # Print the table with separators
    for i, row in enumerate(table):
        formatted_row = ' | '.join(item.ljust(width) for item, width in zip(row, column_widths))
        print(f'{Back.WHITE}{Fore.BLACK}| {formatted_row} |')
        if i == 0:
            separator = '+-' + '-+-'.join('-' * width for width in column_widths) + '-+'
            print(f'{Back.WHITE}{Fore.RED}{separator}')


def __show_item_1__():
    clear_console()
    print(f"{Fore.LIGHTWHITE_EX}{Back.GREEN}1-) Add task{Back.BLACK}\t 2-) Remove Task\n{Back.BLACK}3-) Edit Task\t{Back.BLACK} 4-) Close Console\n")


def __show_item_2__():
    clear_console()
    print(f"{Fore.LIGHTWHITE_EX}{Back.BLACK}1-) Add task\t{Back.GREEN} 2-) Remove Task{Back.BLACK}\n3-) Edit Task\t{Back.BLACK} 4-) Close Console\n")


def __show_item_3__():
    clear_console()
    print(f"{Fore.LIGHTWHITE_EX}{Back.BLACK}1-) Add task\t 2-) Remove Task{Back.BLACK}\n{Back.GREEN}3-) Edit Task{Back.BLACK}\t 4-) Close Console\n")


def __show_item_4__():
    clear_console()
    print(f"{Fore.LIGHTWHITE_EX}{Back.BLACK}1-) Add task\t 2-) Remove Task{Back.BLACK}\n3-) Edit Task{Back.BLACK}\t{Back.GREEN} 4-) Close Console{Back.BLACK}\n")


