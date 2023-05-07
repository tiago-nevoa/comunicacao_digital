import random

# (a) Implemente uma fonte de símbolos genérica, a qual gera ficheiros com N símbolos, de acordo com a Função Massa de
# Probabilidade (FMP) do alfabeto de M símbolos: p(x) = {p(x1), p(x2), . . . , p(xM)}.
# função recebe por ex um dicionário e.g: {'o': 1/2, 'a': 1/4, ...}, N
# M -> número de keys no dicionário

def generic_symbols_source(symb_map, n, file_out):
    letters = []

    for key, value in symb_map.items():
        array = list(int(n * value) * key)
        for elem in array:
            letters.append(elem)

    random.shuffle(letters)

    file = open(file_out, "w")
    for letter in letters:
        file.write(letter)
    file.close()
