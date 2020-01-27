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
        START_TIME = 0
        info_meeting = add(data)
        data.append(info_meeting)
        data_sorted = sorted(
            data, key=lambda element: element[START_TIME])
        storage.write_list_to("meetings.txt", data_sorted)
    elif option == "c":
        cancelation_info = cancel(data)
        storage.write_list_to("meetings.txt", cancelation_info)
        ui.print_result("Meeting canceled.", "")
    elif option == "e":
        editing_info = edit(data)
        storage.write_list_to("meetings.txt", editing_info)
        ui.print_result("Meeting updated.", "")
    elif option == "h":
        total_hours = how_many_hours(data)
        ui.print_result("Total meeting duration (in hours):", total_hours)
    elif option == "m":
        if len(data) == 0:
            ui.print_result("No meetings to compact!", "")
        else:
            compacted_info = compact_meetings(data)
            storage.write_list_to("meetings.txt", compacted_info)
            ui.print_result("Meetings compacted!", "")
    elif option == "q":
        sys.exit(0)
    else:
        raise KeyError


def compact_meetings(schedule):
    """
    Moves meetings to earliest possible time (starting from 8)

    Args:
        schedule (list): list in which meeting should be compacted

    Returns:
        list: list of lists with compacted meetings
    """
    START_TIME = 0
    END_TIME = 1
    meetings_length = len(schedule)
    if int(schedule[0][START_TIME]) != 8:
        # find meeting duration first
        temp = int(schedule[0][START_TIME]) - 8
        schedule[0][START_TIME] = "8"
        schedule[0][END_TIME] = str(int(schedule[0][END_TIME]) - temp)

    for i in range(1, meetings_length):
        # find each meeting duration first
        temp = int(schedule[i][END_TIME]) - int(schedule[i][START_TIME])
        schedule[i][START_TIME] = schedule[i-1][END_TIME]
        schedule[i][END_TIME] = str(int(schedule[i - 1][END_TIME]) + temp)
    return schedule


def how_many_hours(schedule):
    """
    Calculates total meeting duration.

    Args:
        schedule (list): list in which meeting should be updated

    Returns:
        int: total hours of meetings
    """
    START_TIME = 0
    END_TIME = 1
    total_time = 0
    for row in schedule:
        total_time += int(row[END_TIME]) - int(row[START_TIME])
    return total_time


def edit(data):
    """
    Updates specified meeting in the schedule. Ask users for new data.

    Args:
        data (list): list in which meeting should be updated

    Returns:
        list: list of lists with updated meeting
    """
    START_TIME = 0
    start_times = [row[START_TIME] for row in data]
    if len(start_times) == 0:
        ui.print_result("No meetings for today!", "")
        return data
    else:
        while True:
            start_time_update = ui.get_inputs(
                "Edit an existing meeting:", ["Enter the start time"])[START_TIME]
            try:
                if start_time_update in start_times:
                    clear_existing_meeting = [record for record in data if record[START_TIME]
                                              != start_time_update]
                    updated_schedule = add(clear_existing_meeting)

                    clear_existing_meeting.append(updated_schedule)

                    data_sorted = sorted(
                        clear_existing_meeting, key=lambda element: element[START_TIME])
                    return data_sorted
                else:
                    raise ValueError
            except ValueError:
                ui.print_error_message(
                    f"{start_time_update} does not exist in the database!\n")


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
    while True:
        title_duration_start = ui.get_inputs(
            "Schedule a new meeting:", meeting_headers)
        # change meeting duration to end time
        meeting_end = str(int(title_duration_start[START_TIME]) +
                          int(title_duration_start[DURATION_HOURS]))
        try:
            if (check_start(title_duration_start[START_TIME]) and
                    verify_start_overlap(
                        schedule, title_duration_start[START_TIME], meeting_end) and
                    check_duration(title_duration_start[DURATION_HOURS])):
                details = []
                details.append(title_duration_start[START_TIME])
                details.append(meeting_end)
                details.append(title_duration_start[MEETING_TITLE])
                ui.print_result("Meeting added.", "")
                data_sorted = sorted(
                    details, key=lambda element: element[0])
                return data_sorted
            else:
                raise ValueError
        except ValueError:
            if not check_start(title_duration_start[START_TIME]):
                ui.print_error_message(
                    "Meeting is outside of your working hours (8 to 18)!")
            if not verify_start_overlap(schedule, title_duration_start[START_TIME], meeting_end):
                ui.print_error_message(
                    "Meeting overlaps with existing meeting!")
            if not check_duration(title_duration_start[DURATION_HOURS]):
                ui.print_error_message("Duration must be 1 or 2 hours!")


def check_duration(string_element):
    """
    Returns True or False if given element is legit start meeting time

    Args:
        string_element (str): data to work on
    """
    if int(string_element) == 1 or int(string_element) == 2:
        return True
    return False


def check_start(string_element):
    """
    Returns True or False if given element is legit start meeting time

    Args:
        string_element (str): data to work on
    """
    # The meetings should be between 8 and 18
    start_for_verify = int(string_element)
    if start_for_verify >= 8 and start_for_verify <= 18:
        return True
    return False


def verify_start_overlap(data, start_check, end_check):
    """
    Returns True or False if given element is legit start meeting time

    Args:
        data (list): list of list to compare with
        start_check (str): start of meeting
        end_check (str): end of meeting
    """
    START_TIME = 0
    END_TIME = 1
    occupied_hours = []
    for row in data:
        temp = int(row[START_TIME]) + 1
        if int(row[END_TIME]) != temp:
            occupied_hours.extend(
                [int(row[START_TIME]), temp])
        else:
            occupied_hours.append(int(row[START_TIME]))
    # It should not be possible to schedule a meeting that overlaps with existing meeting
    start = int(start_check)
    end = int(end_check) - 1
    if start in occupied_hours or end in occupied_hours:
        return False
    return True


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
    while True:
        start_time_removal = ui.get_inputs(
            "Cancel an existing meeting:", ["Enter the start time"])[START_TIME]
        try:
            if start_time_removal in start_times:
                return [record for record in meeting if record[START_TIME] != start_time_removal]
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
