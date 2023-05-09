# Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt,
# os quais contêm listagens de palavras em Língua Inglesa e Língua Portuguesa.
# Para cada Língua:
# (i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
# (ii) Apresente o valor da entropia de ambos os ficheiros.

import glob
from module1.exercise1d import *
from module1.exercise2b import *

directory = "Word_lists/"
list_of_files = glob.glob(directory + "**")

for file in list_of_files:
    print(file)
    # histogram
    percentages_histogram(file)

    # entropy
    print("Entropy")
    print(f'H = {round(entropy(file), 2)}')

    # blank line to separate files
    print()

