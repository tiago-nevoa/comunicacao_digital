from module1.exercise1c import *

# (d) Função que apresenta o histograma de um ficheiro, o valor da informação própria de cada símbolo e a entropia do ficheiro
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
    plt.title(f'{file}')
    plt.xlabel('Symbol')
    plt.ylabel('Count')
    plt.show()

    print("___________________________________________________________")
    print(self_informations)

    print("___________________________________________________________")
    print("Total entropy: {total_entropy}".format(total_entropy=round(total_entropy, 2)))


histogram("TestFilesCD/a.txt")