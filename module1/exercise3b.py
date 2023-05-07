# (b) Produza sequências com diferentes dimensões N, para valores de N à sua escolha.
# Compare o valor da entropia da fonte, H(X), com o valor estimado para a entropia das sequências geradas.
# Comente os resultados obtidos, em função do par de valores M e N.

import math

# same as exercise3a
def source_entropy(symbol_map):
    total_entropy = 0

    for key in symbol_map:
        entropy = -(symbol_map[key] * math.log(symbol_map[key], 2))
        total_entropy += entropy

    return round(total_entropy, 2)
