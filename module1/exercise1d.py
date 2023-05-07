# (d) Função que apresenta
# o histograma de um ficheiro,
# o valor da informação própria de cada símbolo
# e a entropia do ficheiro
import math
from matplotlib import pyplot as plt
from module1.exercise1c import *

def histogram(file):
    frequencies = symb_frequencies(file)
    plt.bar(frequencies.keys(), frequencies.values())
    plt.title(f'{file}')
    plt.xlabel('Symbol')
    plt.ylabel('Frequency')
    plt.show()


def self_informations(file):
    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))

    self_informations = {}

    for key in frequencies:
        percentage = frequencies[key] / total_frequencies
        self_information = round(math.log(1 / percentage, 2), 2)
        self_informations[key] = self_information

    return self_informations

def entropy(file):
    total_entropy = 0

    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))

    for key in frequencies:
        percentage = frequencies[key] / total_frequencies
        entropy = -(percentage * math.log(percentage, 2))
        total_entropy += entropy

    return total_entropy

