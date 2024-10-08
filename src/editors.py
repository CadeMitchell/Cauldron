"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg
from .utilities import clear as cl
from .file_managment import load_file as lf

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

    def menu(self):
        while True:
            choice = mg([("Exit Meta Editor", "Exit"), ("Edit a Meta Source", "Edit Meta"), ("Add a Meta Source", "Add Source"), ("Delete a Meta Source", "Delete Source")],
                              """A meta is the part of the file that identifies your content. When adding things to your homebrew it will likley refrence things here
                              You may have multiple metas sources per document (I don't recommend this), but for this program you will need atleast 1 source."""
                        )
            
            if choice == "Exit":
                break
            elif choice == "Edit Meta":
                pass
            elif choice == "Add Source":
                self._add_source()
            elif choice == "Delete Source":
                if self.module["sources"].len() > 1:
                    self._delete_source()
                else:
                    input("You only have 1 source. Please add another before attempting to remove the final one.\n(Press ENTER to continue.)")
            
    def _add_source(self):
        new_source = lf("Build_Templates\\_meta.json")["_meta"]["sources"][0]
        user = input("Please enter the unique identifier you would like for your Homebrew file.\nThis must be 6 or more characters, no symbols, unique to all homebrews.\n(Leave INPUT blank to cancel)\nID: ")
        if user:
            new_source["json"] = user
            self.module["sources"].append(new_source)
            input(f"Source {user} added.\n(Press ENTER to continue)\n")
        input("New Source cancelled.\n(Press ENTER to continue)\n")
        
    def _delete_source(self):
        while True:
            sources = [(source["json"], index) for index, source in enumerate(self.module["sources"])]
            choice = mg([("Exit", "Exit")].extend(sources), "Select which source you would like to remove.")
            if choice == "Exit":
                input("Source delete cancelled.\n(Press ENTER to continue)")
                break
            else:
                self.module["sources"].pop(choice)
                input("Source deleted.\n(Press ENTER to continue)")
            
    def _choose_source_menu(self):
        while True:
            sources = [(source["json"], index) for index, source in enumerate(self.module["sources"])]
            choice = mg([("Exit", "Exit")].extend(sources), "Select which source you would like to edit.")
            if choice == "Exit":
                break
            else:
                pass
            
    def _edit_source_menu(self):
        pass