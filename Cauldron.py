import json
import os


class FileManagment:
    current_brew = None
    running = True
    
    def create_file():
        brew = FileManagment.load_file(new_file=True)
        brew = Navigation.new_meta_setup(brew)
        FileManagment.save_file(brew)
        return brew
            
    def load_file(path = None, new_file = False):
        if new_file:
            with open("Build_Templates\\_meta.json", "r") as file:
                brew = json.load(file)
        elif path:
            with open(path, "r") as file:
                brew = json.load(file)
        else:
            files = [(file, FileManagment.load_file("Brews\\"+file)) for file in os.listdir("Brews")] #Start here
            selected = Navigation.menu_generator(files)
            brew = selected
        return brew

    def save_file(brew):
        with open("Brews\\"+brew["_meta"]["sources"][0]["json"]+".json", "w") as file:
                json.dump(brew, file, sort_keys=True, indent=4)


  
def new_meta_setup(brew):
    clear()
    sources = brew["_meta"]["sources"][0]
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
    brew["_meta"]["sources"][0] = sources
    return brew
        
class Editor:
    def edit_schema():
        input(f"This is for refrence only, $Schema is for validating the structure of the file on upload.\n(Press ENTER to leave)\nSchema: {FileManagment.current_brew["$schema"]}")
    
    def edit_meta():
        input("Currently this program only supports the meta for a single book at a time.\nThe meta contains data about the source material. If it is completley original you don't need to worry, its just refrenced as if it were a book.\n(Press ENTER to Continue)\n")
        Navigation.menu_generator()
        
    def edit_action():
        pass
    
    def edit_background():
        pass
    
    def edit_baseitem():
        pass
    
    def edit_boon():
        pass
    
    def edit_class():
        pass

    def edit_classFluff():
        pass
        
    def edit_classfeature():
        pass
    
    def edit_condition():
        pass
    
    def edit_cult():
        pass
    
    def edit_deity():
        pass
    
    def edit_diesease():
        pass
    
    def edit_feat():
        pass
    
    def edit_hazard():
        pass
    
    def edit_item():
        pass
    
    def edit_itemType():
        pass
    
    def edit_itemProperty():
        pass
    
    def edit_language():
        pass
    
    def edit_magicvariant():
        pass
    
    def edit_monster():
        pass
    
    def edit_object():
        pass
    
    def edit_optionalfeature():
        pass
    
    def edit_race():
        pass
    
    def edit_reward():
        pass
    
    def edit_spell():
        pass
    
    def edit_subclass():
        pass
    
    def edit_subclassFeature():
        pass
    
    def edit_subrace():
        pass
    
    def edit_table():
        pass
    
    def edit_varientrule():
        pass
    
    def edit_vehicle():
        pass
        
def Main():
    initialize = Navigation.menu_generator([("Load Homebrew File", FileManagment.load_file), ("Create Homebrew File", FileManagment.create_file)])
    FileManagment.current_brew = initialize()
    brew_editor_lookup={
        "$schema": Editor.edit_schema,
        "_meta": Editor.edit_meta,
        "action": Editor.edit_action,
        "background": Editor.edit_background,
        "baseitem": Editor.edit_baseitem,
        "boon": Editor.edit_boon,
        "class": Editor.edit_class,
        "classFluff": Editor.edit_classFluff,
        "classFeature": Editor.edit_classfeature,
        "condition": Editor.edit_condition,
        "cult": Editor.edit_cult,
        "deity": Editor.edit_deity,
        "disease": Editor.edit_diesease,
        "feat": Editor.edit_feat,
        "hazard": Editor.edit_hazard,
        "item": Editor.edit_item, #This will have some sub categories as their are several keys that fall into this category
        "itemType": Editor.edit_itemType,
        "itemProperty": Editor.edit_itemProperty,
        "language": Editor.edit_language,
        "magicvariant": Editor.edit_magicvariant,
        "monster": Editor.edit_monster,
        "object": Editor.edit_object,
        "optionalfeature": Editor.edit_optionalfeature, #This puts a dict under the _meta key
        "race": Editor.edit_race,
        "reward": Editor.edit_reward,
        "spell": Editor.edit_spell,
        "subclass": Editor.edit_subclass,
        "subclassFeature": Editor.edit_subclassFeature,
        "subrace": Editor.edit_subrace,
        "table": Editor.edit_table,
        "varientrule": Editor.edit_varientrule,
        "vehicle": Editor.edit_vehicle,
    }
    
    while FileManagment.running:
        brew_options = [("Edit " + str(item), brew_editor_lookup[str(item)]) for item in FileManagment.current_brew.keys()]
        choice = Navigation.menu_generator(brew_options)
        clear()
        choice()

    
if __name__ == "__main__":
    clear()
    Main()