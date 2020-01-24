""" User Interface (UI) module """


def main():
    def print_menu(title, list_options, exit_message):
        """
        Displays a menu. Sample output:
            Menu:
                (s) schedule a new meeting
                (c) cancel an existing meeting
                (q) quit

        Args:
            title (str): menu title
            list_options (list): list of strings - options that will be shown in menu
            exit_message (str): the last option with (0) (example: "Back to main menu")

        Returns:
            None: This function doesn't return anything it only prints to console.
        """
        lines_to_print = ["Menu:",
                          "(s) schedule a new meeting",
                          "(c) cancel an existing meeting"
                          "(q) quit"]
        for element in lines_to_print:
            print(element)
        print("\n")


if __name__ == "__main__":
    main()
