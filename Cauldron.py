from typing import Callable
import tkinter as tk
from tkinter import filedialog
import json
import os

def clear():
    os.system("cls")

def create_new_file():
    # Implement file creation logic here
    root = tk.Tk()
    new_File_Path = filedialog.asksaveasfilename(defaultextension=".json", confirmoverwrite=True, initialfile="NewBrew")
    if new_File_Path:
        with open(new_File_Path, "w") as file:
            file.write("Test")
    root.destroy()
            

def open_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path:
        # Implement file opening logic here
        print("Opening file:", file_path)
    root.destroy()

def menu(options: list[tuple[str, Callable]]) -> Callable:
    clear()
    for key, value in enumerate(options):
        print(f"({key+1}) - {value[0]}")
    user = input("Select: ")
    
    for key, value in enumerate(options):
        if int(user)-1 == key:
            return options[int(user)-1][1]
    menu(options)
        

def Main():
    clear()
    test = menu([("Open File", open_file), ("Create New File", create_new_file)])
    test()
    

    
if __name__ == "__main__":
    Main()