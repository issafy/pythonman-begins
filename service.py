import model
import ui
from ui import __show_table__
from model import validate_date, validate_priority
tasks = []


def create_task():
    task_data = read_task()
    task = [task_data[0], task_data[1], task_data[2]]
    tasks.append(task)
    __show_table__(tasks)


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
    return tuple((name, str(priority), due_date))
