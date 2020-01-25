""" User Interface (UI) module for milestoneCalendar"""


def print_menu():
    """
    Displays a menu. Sample output:
        Menu:
            (s) schedule a new meeting
            (c) cancel an existing meeting
            (q) quit

    Args:
        none

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    lines_to_print = ["Menu:",
                      "(s) schedule a new meeting",
                      "(c) cancel an existing meeting",
                      "(e) edit a meeting",
                      "(h) how many hours of meetings",
                      "(q) quit"]
    for element in lines_to_print:
        print(element)


def print_list(schedule):
    """
    Prints table with data.

    Example:
        Your schedule for the day:
        12 - 13 Lunch

    Args:
        schedule (list): list of lists to display

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    START_TIME = 0
    END_TIME = 1
    MEETING_TITLE = 2
    print("\nYour schedule for the day:")
    if len(schedule) == 0:
        print("(empty)\n")
    else:
        for row in schedule:
            print(
                f"{row[START_TIME]} - {row[END_TIME]} {row[MEETING_TITLE]}")
        print("\n")


def get_inputs(title, list_labels):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs("Schedule a new meeting",
                    ["Enter meeting title",
                    "Enter duration in hours (1 or 2)",
                    "Enter start time"])
    Sample display:
        Schedule a new meeting.
        Enter meeting title: <user_input_1>
        Enter duration in hours (1 or 2): <user_input_2>
        Enter start time: <user_input_3>

    Args:
        title (string): title of the "input section"
        list_labels (list): labels of inputs

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print(f"{title}")
    # list which holds the input answers from user
    user_inputs = []
    for item in list_labels:
        user_inputs.append(input(f"{item}: "))
    return user_inputs


def print_result(label, result):
    """
    Displays results of the special functions.

    Args:
        label (str): label of the result
        result: result of the special function (string, number, list or dict)

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f"{label} {result}\n")


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f"ERROR: {message}")
