# run this program from the terminal from the root directory of this project
import ui
import storage
import sys


def choose(data):
    """
    Starts this program and displays its menu.
     * User can access default special features from here.
     * User can exit from here.

     Args:
        data (list): list of lists to be processed.

    Returns:
        None
    """
    user_choice = ui.get_inputs("", ["Your choice"])
    option = user_choice[0]
    if option == "s":
        info_meeting = add(data)
        data.append(info_meeting)
        storage.write_list_to("meetings.txt", data)
    elif option == "c":
        pass
    elif option == "q":
        sys.exit(0)
    else:
        raise KeyError


def add(schedule):
    """
    Asks user for input and adds it into the schedule.

    Args:
        schedule (list): schedule to add new meeting to

    Returns:
        details: list with a new record
    """
    meeting_headers = ["Enter meeting title",
                       "Enter duration in hours (1 or 2)",
                       "Enter start time"]
    duration_meeting = ui.get_inputs(
        "Schedule a new meeting:", meeting_headers)
    # change meeting duration to end time
    MEETING_TITLE = 0
    DURATION_HOURS = 1
    START_TIME = 2
    details = []
    details.append(duration_meeting[START_TIME])
    temp = int(duration_meeting[START_TIME]) + \
        int(duration_meeting[DURATION_HOURS])
    if temp > 23:
        temp -= 24
    details.append(str(temp))
    details.append(duration_meeting[MEETING_TITLE])
    return details


def main():
    while True:
        meetings = storage.get_list_from("meetings.txt")
        ui.print_list(meetings)
        ui.print_menu()
        try:
            choose(meetings)
        except KeyError:
            ui.print_error_message("There is no such option!\n")


if __name__ == "__main__":
    main()
