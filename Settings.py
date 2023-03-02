# Path to the assets folder ONLY
PATH: str = "assets"

import os

# null
def get_path(file: str):
    dirpath = os.path.dirname(__file__)
    dirpath += "\\assets\\"
    filepath = os.path.join(dirpath, file)
    return filepath
