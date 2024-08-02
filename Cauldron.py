from typing import Callable
import json
import os

def clear():
    os.system("cls")

class FileManagment:
    current_brew = None
    running = True
    
    def create_file():
        FileManagment.current_brew = FileManagment.load_file(new_file=True)
        Navigation.new_meta_setup()
        FileManagment.save_file(FileManagment.current_brew)
            
    def load_file(path = None, new_file = False):
        if new_file:
            with open("Build_Templates\\_meta.json", "r") as file:
                brew = json.load(file)
        elif path:
            with open(path, "r") as file:
                brew = json.load(file)
        else:
            files = [(file, Navigation.load_file("Brews\\"+file)) for file in os.listdir("Brews")] #Start here
            Navigation.menu_generator()
            brew = 7
        return brew

    def save_file(brew):
        with open("Brews\\"+brew["_meta"]["sources"][0]["json"]+".json", "w") as file:
                json.dump(brew, file, sort_keys=True, indent=4)


class Navigation: 
    def menu_generator(options: list[tuple[str, Callable]]) -> Callable:
        '''Generates a Menu from a list of tuples.

        Args:
            options (list[tuple[str, Callable]]): str is for the name of the option and callable is a function that will be returned if the item is selected.

        Returns:
            Callable: Returns the selected function.
        '''
        while True:
            clear()
            for index, (option, _) in enumerate(options):
                print(f"({index + 1}) - {option}")
            try:
                choice = int(input("Select an option: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1][1]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
  
    def new_meta_setup():
        clear()
        sources = FileManagment.current_brew["_meta"]["sources"][0]
        input("The setup process for the basic file data is now taking place. This will be documentation related to your homebrew.\nIf you make a mistake or change your mind you will be able to edit this later.\nPress ENTER to continue.")
        clear()
        sources["json"] = input("Please enter a json identifier for your brew file. It must be completely unique to any other homebrew.\nThis is only used as an identifier and will not show up anywhere other than here. Just make it related and unique to the project.\n(Minimum of 6 characters, No Spaces, No Symbols, No Numbers)\nJSON: ")
        clear()
        sources["abbreviation"] = input("Please enter an abbreviation for your brew. (e.g. PHB for 'Player Hand Book')\nAbbreviation: ")
        clear()
        sources["full"] = input("Please enter the full title of the Brew.\nBrew Name: ")
        clear()
        sources["authors"] = input("Please enter the author names for contributers to the source material.\n(Format is as follows: Bob Bowen, Carl Coolguy)\nAuthors: ").split(", ")
        clear()
        sources["convertedBy"] = input("Please enter the names of who converted the source material into a 5eTools compatible json file. (This will most likely just be you since your using this program. Feel free to credit the creator of the program though.)\n(Format is as follows: Bob Bowen, Carl Coolguy)\nConverters: ").split(", ")
        FileManagment.current_brew["_meta"]["sources"][0] = sources
        
        
        
def Main():
    #initialize = Navigation.menu_generator([("Load Homebrew File", FileManagment.load_file), ("Create Homebrew File", FileManagment.create_file)])
    #initialize()
    brew_editor_lookup={
        "_meta": Navigation.edit_meta,
        "action": Navigation.edit_action,
        "background": Navigation.edit_background,
        "boon": Navigation.edit_boon,
        "class": Navigation.edit_class,
        "condition": Navigation.edit_condition,
        "cult": Navigation.edit_cult,
        "deity": Navigation.edit_deity,
        "disease": Navigation.edit_diesease,
        "feat": Navigation.edit_feat,
        "hazard": Navigation.edit_hazard,
        "item": Navigation.edit_item, #This will have some sub categories as their are several keys that fall into this category
        "language": Navigation.edit_meta,
        "object": Navigation.edit_meta,
        "optionalfeature": Navigation.edit_optionalfeature, #This puts a dict under the _meta key
        "race": Navigation.edit_race,
        "reward": Navigation.edit_reward,
        "subclass": Navigation.edit_subclass,
        "table": Navigation.edit_table,
        "varientrule": Navigation.edit_varientrule,
        "vehicle": Navigation.edit_vehicle,
    }
    
    while FileManagment.running:
        brew_options = [("Edit " + str(item), brew_editor_lookup[str(item)]) for item in FileManagment.current_brew.keys()]
        Navigation.menu_generator(brew_options)

    
if __name__ == "__main__":
    clear()
    #Main()