import math
from exercise1 import symb_frequencies
import matplotlib.pyplot as plt

# Para todos os ficheiros do conjunto TestFilesCD.zip,
# apresente o histograma,
# o valor da informação própria de cada símbolo
# e o valor da entropia do ficheiro.


def self_information_and_entropy(file):
    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))

    self_informations = {}
    total_entropy = 0

    for key in frequencies:
        percentage = frequencies[key] / total_frequencies
        # self-information
        symbol_self_information = round(math.log(1 / percentage, 2), 2)
        self_informations[key] = symbol_self_information
        # entropy
        entropy = -(percentage * math.log(percentage, 2))
        total_entropy += entropy

    for key in self_informations:
        print(f'I({key}): {self_informations[key]}')
    print(f'H = {total_entropy}')

    # histogram
    plt.bar(frequencies.keys(), frequencies.values())
    plt.title(file)
    plt.xlabel('Symbol')
    plt.ylabel('Count')
    plt.show()



