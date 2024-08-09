"""
This module is for all things related to all things json file.
"""
import json
import os
import sys
from . import utilities as util

def load_file(path = "") -> dict:
    '''Loads a JSON file from either a given path or from the Brews subfolder.

    Args:
        path (str, optional): Full path to JSON file. Defaults to "".

    Returns:
        dict: Imported JSON file.
    '''
    counter = 0
    while counter < 3:
        try:
            if not path:
                path = util.menu_generator([(file, "Brews\\" + file) for file in os.listdir("Brews")])
            with open(path, "r") as file:
                return json.load(file)
        except Exception as e:
            input(f"Error Occured. If this keeps happening, program will exit after {2-counter} more attempts. (Press ENTER to continue.)\nError: {e}")
            counter += 1
            continue
    sys.exit("Failed to load file after 3 attempts. Exiting program to prevent a infinite loop.")
    
def save_file(brew: dict, path = "Brews"):
    '''Saves homebrew into JSON file

    Args:
        brew (dict): Homebrew data in dictionary.
        path (str, optional): Output folder path. Defaults to "Brews".
    '''
    with open(path + "\\" + brew["_meta"]["sources"][0]["json"] + ".json", "w") as file:
            json.dump(brew, file, sort_keys=True, indent=4)
                
def create_brew_file(brew_id: str):
    '''Creates and saves a new brew file.

    Args:
        brew_id (str): Unique identifier for every homebrew. This needs to be completley unique to all other brews on 5etools. It also must be atleast 6 characters. No Symbols.
    '''
    brew = load_file("Build_Templates\\_meta.json")
    brew["_meta"]["sources"][0]["json"] = brew_id
    save_file(brew)