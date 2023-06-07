import datetime
from datetime import datetime

task_model_deprecated = dict({
    "name": "default_name",
    "priority": 0,
    "due_date": str(datetime.now())
})


def validate_date(due_date: str):
    try:
        parsed_date = datetime.strptime(due_date, "%Y/%m/%d, %H:%M:%S").date()
        return parsed_date
    except ValueError:
        print("The date you entered is not correct. Please try again:\n")
        return 0


def validate_priority(priority: int):
    av = [num for num in range(1, 11)]
    if priority in av:
        return priority
    print("The priority is a number between 1 and 10.\n")
    return -1
