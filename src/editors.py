"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg
from typing import Callable
class base_editor:
    def __init__(self, brew: dict) -> None:
        self.brew = brew
    
    def _edit_string(original_value:str) -> str:
        print(f"Current String Value: {original_value}")
        print(f"(Leave input blank to CANCEL the edit.)")
        user = input("Enter the new value:\n")
        if user:
            input("Value has been changed.\nPress ENTER to continue.\n")
            return user
        input("Value has not been changed.\nPress ENTER to continue.\n")
        return original_value
    
    def _edit_from_list(group: list, editor: Callable):
        while True:
            choice = mg([("Exit", "Exit")].extend([(item[1], item[0]) for item in enumerate(group)]))
            group[choice] = editor(group[choice])
            if choice == "Exit":
                break
        return group
        
    
    def export_module(self):
        return (self.name, self.module)
    
