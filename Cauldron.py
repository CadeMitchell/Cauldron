"""
Main
"""
from src import utilities as util
from src import file_managment as fm
from src import editors as edit
        
def Main():
    brew = {}
    editor_lookup = {"$schema" : edit.schema, "_meta" : edit.schema.edit_schema, "action" : edit.schema.edit_schema, 
                     "background" : edit.schema.edit_schema, "baseitem" : edit.schema.edit_schema, "boon" : edit.schema.edit_schema, 
                     "class" : edit.schema.edit_schema, "classFluff" : edit.schema.edit_schema, "classFeature" : edit.schema.edit_schema, 
                     "condition" : edit.schema.edit_schema, "cult" : edit.schema.edit_schema, "deity" : edit.schema.edit_schema, 
                     "disease" : edit.schema.edit_schema, "feat" : edit.schema.edit_schema, "hazard" : edit.schema.edit_schema, 
                     "item" : edit.schema.edit_schema, "itemType": edit.schema.edit_schema, "itemProperty" : edit.schema.edit_schema, 
                     "language" : edit.schema.edit_schema, "magicvariant" : edit.schema.edit_schema, "monster" : edit.schema.edit_schema, 
                     "object" : edit.schema.edit_schema, "optionalfeature" : edit.schema.edit_schema, "race" : edit.schema.edit_schema, 
                     "reward" : edit.schema.edit_schema, "spell" : edit.schema.edit_schema, "subclass" : edit.schema.edit_schema, 
                     "subclassFeature" : edit.schema.edit_schema, "subrace" : edit.schema.edit_schema, "table" : edit.schema.edit_schema, 
                     "varientrule" : edit.schema.edit_schema, "vehicle": edit.schema.edit_schema,
    }
    
    user = util.menu_generator([("Load Homebrew", 1), ("Create New Homebrew file", 0)])
    if user:
        brew = fm.load_file()
    else:
        hb_id = input("Please enter the unique identifier you would like for your Homebrew file.\nThis must be 6 or more characters, noy symbols, unique to all homebrews.\nID: ")
        fm.create_brew_file(hb_id)
        brew = fm.load_file("Brews\\" + hb_id + ".json")
        
    default_options = [("Add/Remove Modules", 0), ("Save Brew", 1), ("Exit", 2)]
    while brew:
        modules = [(module, editor_lookup[module]) for module in brew.keys()]
        options = default_options.extend(modules)
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
            export = module_editor.export()
            brew[export[0]] = export[1]


if __name__ == "__main__":
    util.clear()
    Main()
