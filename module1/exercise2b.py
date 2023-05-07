# Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt,
# os quais contêm listagens de palavras em Língua Inglesa e Língua Portuguesa.
# Para cada Língua:
# (i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
from matplotlib import pyplot as plt

from module1.exercise1c import *

def percentages_histogram(file):
    frequencies = symb_frequencies(file)
    total_frequencies = float(sum(frequencies.values()))
    percentages = []
    for key in frequencies:
        percentages.append(frequencies[key] / total_frequencies)

    plt.bar(frequencies.keys(), percentages)
    plt.title(f'{file}')
    plt.xlabel('Symbol')
    plt.ylabel('Percentage')
    plt.show()

# (ii) Apresente o valor da entropia de ambos os ficheiros.

#entropy from exercise1d




