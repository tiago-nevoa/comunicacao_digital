import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary

# (ii) BER2, após a aplicação de código de repetição (3, 1) sobre o BSC, em modo de correção;

def repetition_code_bsc_correction_mode(file, error_rate):

    input_bits = []

    with open(file, 'r') as f:
        contents = f.readlines()
        for line in contents:
            input_bits.append(bin(stringToBinary(line)))
    f.close()

    input_bits = "".join(input_bits).replace("0b", "")

    encoded_bits = ''
    for bit in input_bits:
        encoded_bits += bit * 3  # repeat each bit 3 times, as repetition code is (3,1)

    output_bits = binary_symmetric_channel(encoded_bits, error_rate)

    # select only the corrected bits after applying the error correction mechanism
    decoded_bits = ''
    for i in range(0, len(output_bits), 4): # for each sequence of length 4
        sequence = output_bits[i:i+4]
        majority_bit = max(set(sequence), key=sequence.count)  # find the majority bit
        decoded_bits += majority_bit

    # find the total number of bit errors between the original input_bits and the decoded_bits
    total_errors = sum([int(a) != int(b) for a, b in zip(input_bits, decoded_bits)])
    total_bits = len(input_bits)

    BER = round(total_errors / total_bits, 4)

    return BER

# Para a transmissão de cada ficheiro e para todos os valores de p: indique o número total de bits que passam pelo BSC;

# indique o número de símbolos diferentes entre os ficheiros A e B; compare os valores de BER1, BER2 e BER3. Comente
# os resultados.