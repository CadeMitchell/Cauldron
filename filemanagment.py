"""
This module is for all things related to all things json file.
"""

def load_file(a: str, path="") -> dict:
    file = None
    if path:
        