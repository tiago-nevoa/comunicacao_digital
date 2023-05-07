from module1.exercise2b import *
import os
from pathlib import Path

files_path = Path("Word_lists/")
list_of_files = os.listdir("Word_lists/")

for file_name in list_of_files:
    print(f'File: {file_name}')
    self_information_and_entropy(files_path / file_name)
    print()
