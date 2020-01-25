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
        cancelation_info = cancel(data)
        storage.write_list_to("meetings.txt", cancelation_info)
        ui.print_result("Meeting canceled.", "")
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
    MEETING_TITLE = 0
    DURATION_HOURS = 1
    START_TIME = 2
    meeting_headers = ["Enter meeting title",
                       "Enter duration in hours (1 or 2)",
                       "Enter start time"]
    title_duration_start = ui.get_inputs(
        "Schedule a new meeting:", meeting_headers)
    # change meeting duration to end time

    details = []
    details.append(title_duration_start[START_TIME])
    temp = int(title_duration_start[START_TIME]) + \
        int(title_duration_start[DURATION_HOURS])
    if temp > 23:
        temp -= 24
    details.append(str(temp))
    details.append(title_duration_start[MEETING_TITLE])
    ui.print_result("Meeting added.", "")
    return details


def cancel(meeting):
    """
    Remove a record with a given id from the table.

    Args:
        meeting (list): list of lists to remove a record from

    Returns:
        list: list of lists without specified record.
    """
    START_TIME = 0
    start_times = [row[START_TIME] for row in meeting]
    print(f'start_times = {start_times}')
    while True:
        start_time_removal = ui.get_inputs(
            "Cancel an existing meeting:", ["Enter the start time"])[START_TIME]
        print(f'start_time_removal = {start_time_removal}')
        try:
            if start_time_removal in start_times:
                return [record for record in meeting if record[0] != start_time_removal]
            else:
                raise ValueError
        except ValueError:
            ui.print_error_message(
                f"{start_time_removal} does not exist in the database!\n")


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
