# coding=utf-8
#!/usr/bin/env python
import math
from pathlib import Path
import matplotlib.pyplot as plt

files_path = Path("TestFilesCD/")

# (a) Função que apresenta os primeiros N termos da progressão geométrica de primeiro termo u e razão r. Os valores de N, u e r são passados como parâmetro.

def first_n_terms_gs(u, r, N):
    terms = [u]
    for num in range(1,N):
        term = u * r**num
        terms.append(term)
    return terms


# print(first_n_terms_gs(3, 2, 5))


# (b) Função que determina o máximo divisor comum entre dois números inteiros a e b, através do algoritmo de Euclides.
def sort(a, b):
    if a < b:
        aux = a
        a = b
        b = aux


def mdc(a, b):
    a = abs(a)
    b = abs(b)
    sort(a, b)
    remainder = a
    while remainder > 0:
        remainder = a % b
        a = b
        b = remainder
    return a

# print("mdc =", mdc(92, -138))

# (c) Função que identifica os símbolos mais frequente e menos frequente de um ficheiro passado como parâmetro, indicando a frequência de ocorrência desses dois símbolos.

def symb_frequencies(file):
    frequencies = {}
    with open(file, "r", errors='ignore') as f:
        lines = f.readlines()
        for line in lines:
            symbols = list(line.strip().replace(" ", ""))
            for char in symbols:
                if frequencies.setdefault(char) == None:
                    frequencies[char] = 1
                else:
                    frequencies[char] += 1
        f.close()
    return frequencies


def most_and_least_frequent(file):
    frequencies = symb_frequencies(file)

    biggest = sorted(frequencies.values())[-1]
    smallest = sorted(frequencies.values())[0]

    most_freq = list(frequencies.keys())[list(frequencies.values()).index(biggest)]
    least_freq = list(frequencies.keys())[list(frequencies.values()).index(smallest)]

    return { most_freq: biggest, least_freq: smallest }

print(most_and_least_frequent(files_path / "alice29.txt"))


# (d) Função que apresenta o histograma de um ficheiro, o valor da informação própria de cada símbolo e a entropia do ficheiro

import matplotlib.pyplot as plt
import math


def histogram(file):
    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))

    self_informations = []
    total_entropy = 0

    # create lists for histogram data
    keys = []
    counts = []

    for key in frequencies:
        percentage = frequencies[key] / total_frequencies
        self_information = round(math.log(1 / percentage, 2), 2)
        self_informations.append(self_information)

        entropy = -(percentage * math.log(percentage, 2))
        total_entropy += entropy

        frequency = int(frequencies[key])

        keys.append(key)
        counts.append(frequency)

    # plot histogram
    plt.bar(keys, counts)
    plt.title('Histogram')
    plt.xlabel('Symbol')
    plt.ylabel('Count')
    plt.show()

    print("___________________________________________________________")
    print(self_informations)

    print("___________________________________________________________")
    print("Total entropy: {total_entropy}".format(total_entropy=round(total_entropy, 2)))


histogram(files_path / "a.txt")