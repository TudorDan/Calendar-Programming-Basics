# run this program from the terminal from the root directory of this project
import ui
import storage
import sys


def choose():
    user_choice = ui.get_inputs("", ["Your choice"])
    option = user_choice[0]
    if option == "s":
        pass
    elif option == "c":
        pass
    elif option == "q":
        sys.exit(0)
    else:
        raise KeyError("There is no such option!\n")


def main():
    schedule = storage.get_list_from("meetings.txt")
    ui.print_result("Your schedule for the day", schedule)
    while True:
        ui.print_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
