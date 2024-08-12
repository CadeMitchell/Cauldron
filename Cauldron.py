"""
Main
"""
from src import utilities as util
from src import file_managment as fm
        
def Main():
    brew = {}
    brew_keys = ["$schema", "_meta", "action", "background", "baseitem", "boon", "class", "classFluff", 
                  "classFeature", "condition", "cult", "deity", "disease", "feat", "hazard", "item", "itemType", 
                  "itemProperty", "language", "magicvariant", "monster", "object", "optionalfeature", "race", 
                  "reward", "spell", "subclass", "subclassFeature", "subrace", "table", "varientrule", "vehicle"]

    
    user = util.menu_generator([("Load Homebrew", 1), ("Create New Homebrew file", 0)])
    if user:
        brew = fm.load_file()
    else:
        hb_id = input("Please enter the unique identifier you would like for your Homebrew file.\nThis must be 6 or more characters, noy symbols, unique to all homebrews.\nID: ")
        fm.create_brew_file(hb_id)
        brew = fm.load_file("Brews\\" + hb_id + ".json")
        
    while brew:
        default_options = [("Add/Remove Categories", 1), ("Save Brew", 1), ("Exit", 1)]
        
        choice = util.menu_generator()
        choice()

if __name__ == "__main__":
    util.clear()
    Main()
