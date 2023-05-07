# Para todos os ficheiros do conjunto TestFilesCD.zip,
# apresente o histograma,
# o valor da informação própria de cada símbolo
# e o valor da entropia do ficheiro.

import glob
from module1.exercise1d import *

directory = "TestFilesCD/"
list_of_files = glob.glob(directory + "**")

for file in list_of_files:
    print(file)
    # histogram
    histogram(file)

    # self-information
    print("Self-information")
    for key in self_informations(file):
        print(f'I({key}) = {self_informations(file)[key]}')

    # entropy
    print("Entropy")
    print(f'H = {round(entropy(file), 2)}')

    # blank line to separate files
    print()
