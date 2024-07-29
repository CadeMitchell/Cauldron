
from tkinter import filedialog

import json
import os

def clear():
    os.system("cls")

def create_new_file():
    # Implement file creation logic here
    new_File_Path = filedialog.asksaveasfilename(defaultextension=".json", confirmoverwrite=True, initialfile="NewBrew")
    if new_File_Path:
        with open(new_File_Path, "w") as file:
            file.write("Test")
            

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Implement file opening logic here
        print("Opening file:", file_path)

def menu(options: list[tuple[str,function]]):
    clear()
    for key, value in enumerate(options):
        print(f"({key}) - {value[0]}")
    user = input("Option: ", end = "")
        
def Main():
    clear()
    
    
if __name__ == "__main__":
    Main()