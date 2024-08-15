"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg

class base_editor:
    def __init__(self, brew: dict) -> None:
        self.options = [("Exit", 0)]
        self.name = None
        self.module = brew
    
    def export_module(self):
        return (self.name, self.module)
    

class schema(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.name = "$schema"
        self.module = brew["$schema"]
        self.options.extend([("Edit Schema", self.edit_schema), ("Reset Schema to Default", self.reset_to_default)])
        
    def menu(self):
        while True:
            choice = mg(self.options)
            if choice == 0:
                break
            else:
                choice()

    def edit_schema(self):
        print(f"Current $Schema: {self.module}")
        if input(f"Warning. Changing $Schema is advised against. Do not change under normal circumstances.\n(Y) to continue to edit.\n(N) to cancel\n").upper() == "Y":
            self.module = input("Enter new $Schema URL:\n")
            input("$schema has been changed.\nPress ENTER to continue.\n")
            
    def reset_to_default(self):
        self.module = "https://raw.githubusercontent.com/TheGiddyLimit/5etools-utils/master/schema/brew-fast/homebrew.json"
        input("$schema has been reset to default.\nPress ENTER to continue.\n")

class meta(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)