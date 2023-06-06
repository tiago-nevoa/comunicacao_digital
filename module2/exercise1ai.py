# Sobre a implementação do Binary Symmetric Channel (BSC), apresentado na Figura 1 (a),
# considere os valores de probabilidade de erro de bit p  {10^-1; 10^2; 10^-3; 10^-4; 10^-5}.
# Na transmissão de quatro ficheiros à sua escolha,
# usando o diagrama apresentado na Figura 1 (b), calcule os seguintes valores de BER:
# (i) BER1, entre a entrada e a saída do BSC, sem controlo de erros;

# Para a transmissão de cada ficheiro e para todos os valores de p:
# indique o número total de bits que passam pelo BSC;
# indique o número de símbolos diferentes entre os ficheiros A e B;
# compare os valores de BER1, BER2 e BER3.
# Comente os resultados.

from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary

input_bits = []

def calculate_BER(file, error_rate):
    input_bits = []

    with open(file, 'r') as f:
        contents = f.readlines()
        for line in contents:
            input_bits.append(bin(stringToBinary(line)))
    f.close()

    input_bits = "".join(input_bits).replace("0b", "")
    output_bits = binary_symmetric_channel(input_bits, error_rate)

    results = [(ord(a) ^ ord(b)) for a, b in zip(input_bits, output_bits)]

    total_errors = len([num for num in results if num == 1])
    total_bits = len(list(output_bits))

    BER = round(total_errors / total_bits, 7)
    return BER