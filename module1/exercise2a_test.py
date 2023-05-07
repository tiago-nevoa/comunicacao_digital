from module1.exercise2a import self_information_and_entropy
import os
from pathlib import Path

files_path = Path("TestFilesCD/")
list_of_files = os.listdir("TestFilesCD/")

for file_name in list_of_files:
    print(f'File: {file_name}')
    self_information_and_entropy(files_path / file_name)
    print()
