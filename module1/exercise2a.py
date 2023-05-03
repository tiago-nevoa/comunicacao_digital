import math
import os
from pathlib import Path
from exercise1 import symb_frequencies

# Para todos os ficheiros do conjunto TestFilesCD.zip,
# apresente o histograma,
# o valor da informação própria de cada símbolo
# e o valor da entropia do ficheiro.

files_path = Path("TestFilesCD/")
list_of_files = os.listdir(files_path)

def self_information_and_entropy(file):
    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))

    self_informations = []
    total_entropy = 0

    for key in frequencies:
        percentage = frequencies[key] / total_frequencies
        # self-information
        symbol_self_information = round(math.log(1 / percentage, 2), 2)
        self_informations.append(symbol_self_information)
        # entropy
        entropy = -(percentage * math.log(percentage, 2))
        total_entropy += entropy

    print(f'Self-informations: {self_informations}')
    print(f'H = {total_entropy}')


for file in list_of_files:
    print(f'File: {file}')
    self_information_and_entropy(files_path / file)
    print()
