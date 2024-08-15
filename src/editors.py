"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg

class base_editor:
    def __init__(self, brew: dict) -> None:
        self.default_options = [("Exit", 0)]
        self.name = None
        self.module = brew
    
    def export_module(self):
        return (self.name, self.module)
    

class schema(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.name = "$schema"
        self.module = brew["$schema"]
        
    def menu(self):
        while True:
            choice = mg(self.default_options.extend([("Edit Schema", self.edit_schema)]))
            if choice == 0:
                break
            else:
                choice()

    def edit_schema(self):
        print(f"Current $Schema: {self.module}")
        if input(f"Warning. Changing $Schema is advised against.\n(Y) to continue to edit.\n(N) to cancel").upper() == "Y":
            self.module = input("Enter new $Schema URL:\n")
            
    def reset_to_default(self):
        self.module = "https://raw.githubusercontent.com/TheGiddyLimit/5etools-utils/master/schema/brew-fast/homebrew.json"
            