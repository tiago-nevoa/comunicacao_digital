# (d) Função que apresenta
# o histograma de um ficheiro,
# o valor da informação própria de cada símbolo
# e a entropia do ficheiro

from module1.exercise1d import *

file = "TestFilesCD/a.txt"

# histogram
histogram(file)

# self-information
print("Self-information")
for key in self_informations(file):
    print(f'I({key}) = {self_informations(file)[key]}')

# entropy
print("Entropy")
print(f'H({file}) = {entropy(file)}')
