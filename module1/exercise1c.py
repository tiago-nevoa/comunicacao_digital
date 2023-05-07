# coding=utf-8
#!/usr/bin/env python
import math
from pathlib import Path
import matplotlib.pyplot as plt

files_path = Path("TestFilesCD/")

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

