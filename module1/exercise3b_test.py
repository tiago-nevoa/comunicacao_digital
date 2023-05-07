# (b) Produza sequências com diferentes dimensões N, para valores de N à sua escolha.
# Compare o valor da entropia da fonte, H(X), com o valor estimado para a entropia das sequências geradas.
# Comente os resultados obtidos, em função do par de valores M e N.

from module1.exercise1d import *
from module1.exercise3a import *
from module1.exercise3b import *


symbol_map = {'a': 1 / 2, 'b': 1 / 4, 'c': 1 / 8, 'd': 1 / 8}
# source entropy
print(f'H(source) = {source_entropy(symbol_map)}')

# sequence 1
N = 16
file_out = "Output_Files/exercise3_sequence1.txt"
# generate sequence
generic_symbols_source(symbol_map, N, file_out)
# sequence entropy
print(f'H(sequence1) = {entropy(file_out)}')

# sequence 2
N = 653
file_out = "Output_Files/exercise3_sequence2.txt"
# generate sequence
generic_symbols_source(symbol_map, N, file_out)
# sequence entropy
print(f'H(sequence2) = {entropy(file_out)}')

# sequence 3
N = 95616
file_out = "Output_Files/exercise3_sequence3.txt"
# generate sequence
generic_symbols_source(symbol_map, N, file_out)
# sequence entropy
print(f'H(sequence3) = {entropy(file_out)}')
