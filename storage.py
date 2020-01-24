""" Storage (saving and loading) module for milestoneCalendar"""


def get_list_from(file_name):
    """
    Reads txt file and returns it as a list of lists.
    Lines are rows columns that are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
        current_list (list): List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    current_list = [element.replace("\n", "").split(";") for element in lines]
    return current_list


def write_list_to(file_name, new_list):
    """
    Writes list of lists into a txt file.

    Args:
        file_name (str): name of file to write to
        new_list(list): list of lists to write to a file

    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in new_list:
            row = ';'.join(record)
            file.write(row + "\n")
