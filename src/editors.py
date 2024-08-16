"""
This module if for housing the editor class and its subclasses for each editor.
"""
from .utilities import menu_generator as mg

class base_editor:
    def __init__(self, brew: dict) -> None:
        self.options = [("Exit", 0)]
        self.options_action = [("Exit", 0)]
        self.options_entries = [("Exit", 0)]
        self.options_time = [("Exit", 0)]
        self.name = None
        self.module = brew
        self.brew = brew
    
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
            user = input("(Leave Blank to Cancel)\nEnter new $Schema URL:\n")
            if user:
                self.module = user
                input("$schema has been changed.\nPress ENTER to continue.\n")
            else:
                input("$schema has not been changed.\nPress ENTER to continue.\n")
            
    def reset_to_default(self):
        self.module = "https://raw.githubusercontent.com/TheGiddyLimit/5etools-utils/master/schema/brew-fast/homebrew.json"
        input("$schema has been reset to default.\nPress ENTER to continue.\n")

class meta(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.name = "_meta"
        self.module = brew["_meta"]["sources"][0]
        self.options.extend([("Edit Full Brew Name", self.edit_full), ("Edit Brew Abbreviation", self.edit_abbreviation),
                             ("Edit Brew ID", self.edit_json), ("Edit Version", self.edit_version), ("Edit Brew Color", self.edit_color)
                             ("Edit Authors", self.edit_authors)])
        
    def menu(self):
        while True:
            choice = mg(self.options)
            if choice == 0:
                break
            else:
                choice()
    
    def edit_full(self):
        user = input("(Leave Blank to Cancel)\nEnter the new full Homebrew Name/Title:\n")
        if user:
            self.module["full"] = user
            input("Brew name has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew name has not been changed.\nPress ENTER to continue.\n")
            
    def edit_abbreviation(self):
        user = input("(Leave Blank to Cancel)\nEnter the new Hombrew Abbreviation:\n")
        if user:
            self.module["abbreviation"] = user
            input("Brew Abbreviation has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew Abbreviation has not been changed.\nPress ENTER to continue.\n")
            
    def edit_json(self):
        user = input("(Leave Blank to Cancel)\nThis must be 6 or more characters, no symbols, unique to all homebrews.\nChanging this will require you to change this everywhere it is refenced manually.\nEnter the new Hombrew ID:\n")
        if user:
            self.module["json"] = user
            input("Brew ID has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew ID has not been changed.\nPress ENTER to continue.\n")
            
    def edit_version(self):
        user = input("(Leave Blank to Cancel)\nEnter the new version number:\n")
        if user:
            self.module["version"] = user
            input("Brew version number has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew version number has not been changed.\nPress ENTER to continue.\n")
            
    def edit_color(self):
        user = input("(Leave Blank to Cancel)\nEnter the new brew color scheme in 5etools:\n")
        if user:
            self.module["color"] = user
            input("Brew color scheme has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew color scheme has not been changed.\nPress ENTER to continue.\n")
            
    def edit_authors(self):
        user = input("(Leave Blank to Cancel)\nEnter the authors seperated by commas (e.g Bob Glass, Robert Valium, Test Dummy):\n")
        if user:
            self.module["authors"] = user.split(", ")
            self.module["convertedBy"] = user.split(", ")
            input("Brew color scheme has been changed.\nPress ENTER to continue.\n")
        else:
            input("Brew color scheme has not been changed.\nPress ENTER to continue.\n")
            
    def export_module(self):
        module = self.brew["_meta"]["sources"][0] == self.module
        
        return (self.name, module)
    
class action(base_editor):
    def __init__(self, brew: dict) -> None:
        super().__init__(brew)
        self.name = "action"
        self.module = brew["action"]
        self.options.extend([("Add Action", self.action_add,) ("Edit Action", self.action_edit)])
        self.options_action.extend([("Edit Action Name", self.edit_name), ("Edit Entries", self.edit_entries), ("Edit Time", self.edit_time)])
        self.options_entries.extend([])
        self.options_time.extend([])
        
    def menu(self):
        while True:
            choice = mg(self.options)
            if choice == 0:
                break
            else:
                choice()

    def action_add(self):
        user = input("(Leave Blank to Cancel)\nEnter the name of the new action\n")
        if user:
            self.module.append({"source": self.brew["_meta"][0]["source"], "name": user, "page": 0, "entries": [], "time": []})
            input(f"Action {user} has been created.\nPress ENTER to continue.\n")
        else:
            input("Action has not been created.\nPress ENTER to continue.\n")
                 
    def action_edit(self):
        while True:
            options = [("Exit", "0")]
            options.extend([(action[1]["name"], action[0]) for action in enumerate(self.module)])
            selected_action = mg(options)
            if selected_action == "0":
                break
            else:
                action = self.module[selected_action]
                while True:
                    selected_edit = mg(self.options_action)
                    if selected_action == 0:
                        break
                    else:
                        self.module[selected_action] = selected_edit(action)
             
    def edit_name(self, action):
        user = input("(Leave Blank to Cancel)\nEnter the Action's new name:\n")
        if user:
            action["name"] = user
            input("Action name has been changed.\nPress ENTER to continue.\n")
        else:
            input("Action name has not been changed.\nPress ENTER to continue.\n")
        return action
    
    def edit_entries(self, action):
        while True:
            options = [("Exit", "0")]
            options.extend([(action[1]["name"], action[0]) for action in enumerate(self.module)])
            selected_action = mg(options)
            if selected_action == "0":
                break
            else:
                action = self.module[selected_action]
                while True:
                    selected_edit = mg(self.options_action)
                    if selected_action == 0:
                        break
                    else:
                        self.module[selected_action] = selected_edit(action)
        return action
    
    def edit_time(self, action):
        
        return action