import math
import os
from pathlib import Path
from exercise2a import self_information_and_entropy

# Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt,
# os quais contêm listagens de palavras em Língua Inglesa e Língua Portuguesa.
# Para cada Língua:
# (i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
# (ii) Apresente o valor da entropia de ambos os ficheiros.

files_path = Path("Word_lists/")
list_of_files = os.listdir(files_path)

for file in list_of_files:
    print(f'File: {file}')
    self_information_and_entropy(files_path / file)
    print()

