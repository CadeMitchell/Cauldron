"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg
from .utilities import clear as cl
from typing import Callable

class base_editor:
    def __init__(self, brew: dict) -> None:
        self.brew = brew
        self.module = brew
    
    def export_module(self):
        return (self.name, self.module)
    
    def _edit_string(original_value: str) -> str:
        cl()
        print(f"Current String Value: {original_value}")
        print(f"(Leave input blank to CANCEL the edit.)")
        user = input("Enter the new value:\n")
        if user:
            input("Value has been changed.\nPress ENTER to continue.\n")
            return user
        input("Value has not been changed.\nPress ENTER to continue.\n")
        return original_value
    
    def _edit_int(original_int: int):
        while True:
            cl()
            try:
                print(f"Current Number Value: {original_int}")
                print(f"(Leave input blank to CANCEL the edit.)")
                user = input("Enter the new value:\n")
                if user:
                    user = int(user)
                    input("Value has been changed.\nPress ENTER to continue.\n")
                    return user
                else:
                    break
            except:
                    input("No number detected, try again.\nPress ENTER to continue.\n")
                    continue
        input("Value has not been changed.\nPress ENTER to continue.\n")
        return original_int
        
    def _edit_set_choice(original_choice: object, options: list[(str, str)], prompt = ""):
        choice = mg([("Cancel Change", "Cancel")].extend(options), prompt)
        if choice == "Cancel":
            return original_choice
        else:
            return choice

class schema_editor(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.module = brew["$schema"]
        
    def menu(self):
        while True:
            choice = mg([("Exit Schema Editor", "Exit"), ("Edit Shema", "Schema"), ("Reset Schema", "Reset")], 
                        f"Highly Reccomend not to change Schema, Do so at your own risk.\nCurrent Schema: {self.module}"
                        )
            if choice == "Exit":
                break
            elif choice == "Scehma":
                self.module = schema_editor._edit_string(self.module)
            elif choice == "Reset":
                self.module = "https://raw.githubusercontent.com/TheGiddyLimit/5etools-utils/master/schema/brew-fast/homebrew.json"
                
class meta_editor(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.module = brew["_meta"]
        self.primary_meta = self.module[0]

    def menu(self):
        while True:
            choice = mg([("Exit Meta Editor", "Exit"), ("Edit a Meta Source", "Edit Meta"), ("Add a Meta Source", "Add Meta"), ("Delete a Meta Source", "Delete Meta")],
                              """A meta is the part of the file that identifies your content. When adding things to your homebrew it will likley refrence things here
                              You may have multiple metas per document (I don't recommend this), but for this program you will have a primary meta for file sorting purposes."""
                              )
            
            if choice == "Exit":
                break
            elif choice == "Edit Meta":
                pass
            elif choice == "Add Meta":
                pass
            elif choice == "Delete Meta":
                pass