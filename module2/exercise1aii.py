import sys
import os

import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary

# (ii) BER2, após a aplicação de código de repetição (3, 1) sobre o BSC, em modo de correção;

def BER_repetition_code_bsc_correction_mode(file, error_rate, repetition_code):
    with open(file, 'r') as input_file:
        contents = input_file.read()

    input_bits=bin(stringToBinary(contents)).replace("0b","")
    encoded_bits = ''
    for bit in input_bits:
        encoded_bits += bit * repetition_code  # repeat each bit 3 times, as repetition code is (3,1)

    output_bits = binary_symmetric_channel(encoded_bits, error_rate)

    # select only the corrected bits after applying the error correction mechanism
    decoded_bits = ''
    for i in range(0, len(output_bits), repetition_code): # for each sequence of length 4
        sequence = output_bits[i:i+repetition_code]
        majority_bit = max(set(sequence), key=sequence.count)  # find the majority bit
        decoded_bits += majority_bit

    # find the total number of bit errors between the original input_bits and the decoded_bits
    total_errors = sum([int(a) != int(b) for a, b in zip(input_bits, decoded_bits)])
    total_bits = len(input_bits)

    BER = np.double(total_errors / total_bits)

    return BER

def count_bits_through_BSC(file, repetition_code):
    with open(file, 'rb') as input_file:
        contents = input_file.read()
        file_bits = len(contents) * 8 * repetition_code  # *8 because Python reads file in bytes
    return file_bits


# Para a transmissão de cada ficheiro e para todos os valores de p: indique o número total de bits que passam pelo BSC;

# indique o número de símbolos diferentes entre os ficheiros A e B; compare os valores de BER1, BER2 e BER3. Comente
# os resultados.