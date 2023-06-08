import model
import ui
import colorama
from colorama import Back, Fore, Style
from ui import __show_table__
from model import validate_date, validate_priority
tasks = [['Task Test', '!!!!      ', '2023/11/11, 13:00:00', 'False']]


def __task_count__():
    return len(tasks)


def create_task():
    task_data = read_task()
    task = [task_data[0], task_data[1], task_data[2], task_data[3]]
    tasks.append(task)


def read_task():
    name = input("What is the name of the task?\n")
    print("The task name: {}".format(name))

    priority = int(input("What is the priority of the task?\n"))
    while validate_priority(priority) == -1:
        int(input("What is the priority of the task?\n"))
    print("The task priority: {}".format(priority))

    due_date = input("Give the date in this format and all\nnumeric value: year/month/day, hour-minutes-seconds\n")
    while validate_date(due_date) == 0:
        due_date = input("Give the date in this format and all\nnumeric value: year/month/day, hour-minutes-seconds\n")

    completed = False
    return tuple((
        name,
        '!' * priority + ' ' * (10 - priority),
        due_date,
        str(completed)
    ))


def __check_task__():
    task_name = input("What is the name of the task?\n")

    for i in range(len(tasks)):
        print(f'Precision: |{tasks[i][3]}|')
        if tasks[i][0] != task_name:
            print(f'{Back.LIGHTRED_EX}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Task with name: {task_name} does not exist.')
        elif tasks[i][0] == task_name:
            if 'False' in tasks[i][3]:
                tasks[i][3] = f'{Back.LIGHTGREEN_EX} True {Back.LIGHTWHITE_EX}  '
            else:
                tasks[i][3] = f'{Back.LIGHTRED_EX} False {Back.LIGHTWHITE_EX} '


