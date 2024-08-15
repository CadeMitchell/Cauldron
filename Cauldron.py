"""
Main
"""
from src import utilities as util
from src import file_managment as fm
from src import editors as edit
        
def Main():
    brew = {}
    editor_lookup = {"$schema" : edit.schema, "_meta" : edit.meta, "action" : edit.schema, 
                     "background" : edit.schema, "baseitem" : edit.schema, "boon" : edit.schema, 
                     "class" : edit.schema, "classFluff" : edit.schema, "classFeature" : edit.schema, 
                     "condition" : edit.schema, "cult" : edit.schema, "deity" : edit.schema, 
                     "disease" : edit.schema, "feat" : edit.schema, "hazard" : edit.schema, 
                     "item" : edit.schema, "itemType": edit.schema, "itemProperty" : edit.schema, 
                     "language" : edit.schema, "magicvariant" : edit.schema, "monster" : edit.schema, 
                     "object" : edit.schema, "optionalfeature" : edit.schema, "race" : edit.schema, 
                     "reward" : edit.schema, "spell" : edit.schema, "subclass" : edit.schema, 
                     "subclassFeature" : edit.schema, "subrace" : edit.schema, "table" : edit.schema, 
                     "varientrule" : edit.schema, "vehicle": edit.schema,
    }
    
    user = util.menu_generator([("Load Homebrew", 1), ("Create New Homebrew file", 0)])
    if user:
        brew = fm.load_file()
    else:
        hb_id = input("Please enter the unique identifier you would like for your Homebrew file.\nThis must be 6 or more characters, noy symbols, unique to all homebrews.\nID: ")
        fm.create_brew_file(hb_id)
        brew = fm.load_file("Brews\\" + hb_id + ".json")
        
   
    while brew:
        options = [("Add/Remove Modules", 0), ("Save Brew", 1), ("Exit", 2)]
        modules = [(module, editor_lookup[module]) for module in brew.keys()]
        options.extend(modules)
        choice = util.menu_generator(options)
        if choice == 0:
            pass
        elif choice == 1:
            fm.save_file(brew)
            input("Your Homebrew File has been saved!\n(Press ENTER to continue)")
        elif choice == 2:
            break
        else:
            module_editor = choice(brew)
            module_editor.menu()
            export = module_editor.export_module()
            brew[export[0]] = export[1]


if __name__ == "__main__":
    util.clear()
    Main()
