"""
Main
"""
import os
from src import utilities as util
from src import file_managment as fm

class Editor:
    def edit_schema():
        pass    
    def edit_meta():
        pass        
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
    brew = {}
    user = util.menu_generator([("Load Homebrew", 1), ("Create New Homebrew file", 0)])
    if user:
        brew = fm.load_file()
    else:
        hb_id = input("Please enter the unique identifier you would like for your Homebrew file.\nThis must be 6 or more characters, noy symbols, unique to all homebrews.\nID: ")
        fm.create_brew_file(hb_id)
        brew = fm.load_file("Brews\\" + hb_id + ".json")
        
    input(brew)

if __name__ == "__main__":
    util.clear()
    Main()
    


    
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