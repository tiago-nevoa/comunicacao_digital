# (c) Função que identifica os símbolos mais frequente e menos frequente de um ficheiro passado como parâmetro,
# indicando a frequência de ocorrência desses dois símbolos.

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

    greatest = sorted(frequencies.values())[-1]
    smallest = sorted(frequencies.values())[0]

    most_freq = list(frequencies.keys())[list(frequencies.values()).index(greatest)]
    least_freq = list(frequencies.keys())[list(frequencies.values()).index(smallest)]

    return { most_freq: greatest, least_freq: smallest }


