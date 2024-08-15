"""
This module is for providing general utilities.
"""
import os

def clear():
    '''Clears the Console
    '''
    os.system("cls")

def menu_generator(options: list[tuple[str, object]], prompt = "") -> object:
        '''Generates a Menu from a list of tuples.

        Args:
            options (list[tuple[str, Callable]]): str is for the name of the option and object will be returned if the item is selected.
            prompt (str): Provides a prompt for the user in addition to the options.

        Returns:
            object: Returns the selected object.
        '''
        while True:
            clear()
            if prompt:
                print(prompt)
            for index, (option, _) in enumerate(options):
                print(f"({index + 1}) - {option}")
            try:
                choice = int(input("Select an option: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1][1]
                else:
                    print("Invalid choice. Please try again.\n(Press ENTER to continue)")
            except ValueError:
                input("Invalid input. Please enter a number.\n(Press ENTER to continue)")