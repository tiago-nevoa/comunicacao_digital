import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary


# (ii) BER3, após a aplicação de código de Hamming (7, 4) sobre o BSC, em modo de correção;

def BER_hamming_code_bsc_correction_mode(file, error_rate):
    with open(file, 'r') as input_file:
        contents = input_file.read()
        input_bits = bin(stringToBinary(contents)).replace("0b", "").zfill(3)

    encoded_bits = []

    # Encode the input bits using Hamming (7, 4) code
    for i in range(0, len(input_bits), 4):
        # Check if there are enough bits remaining to form a complete group
        if i + 4 > len(input_bits):
            break

        message = input_bits[i:i + 4]

        # Calculate parity bits
        parity_0 = str(int(message[1]) ^ int(message[2]) ^ int(message[3]))
        parity_1 = str(int(message[0]) ^ int(message[1]) ^ int(message[3]))
        parity_2 = str(int(message[0]) ^ int(message[2]) ^ int(message[3]))

        # Construct the encoded bits
        encoded_bits += [message, parity_0, parity_1, parity_2]

    output_bits = binary_symmetric_channel("".join(encoded_bits), error_rate)

    decoded_bits = ''
    error_positions = []
    transpose_parity_matrix = [[1, 0, 0],
                               [1, 0, 1],
                               [0, 1, 1],
                               [1, 1, 1],
                               [1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]]

    # Decode the received bits
    for i in range(0, len(output_bits), 7):
        # Check if there are enough bits remaining to form a complete group
        if i + 7 > len(output_bits):
            break

        codeword = output_bits[i:i + 7]


        # Calculate syndrome bits
        syndrome_0 = str(int(codeword[0]) ^ int(codeword[1]) ^ int(codeword[3]) ^ int(codeword[4]))
        syndrome_1 = str(int(codeword[0]) ^ int(codeword[2]) ^ int(codeword[3]) ^ int(codeword[5]))
        syndrome_2 = str(int(codeword[1]) ^ int(codeword[2]) ^ int(codeword[3]) ^ int(codeword[6]))
        syndrome = [syndrome_2, syndrome_1, syndrome_0]

        # Check if any error occurred
        if int(syndrome_2 + syndrome_1 + syndrome_0, 2) != 0:
            # Error detected, find the position of the error
            for index, line in enumerate(transpose_parity_matrix):
                    if syndrome == line:
                        error_positions += index

            # error_position = int(syndrome_2 + syndrome_1 + syndrome_0, 2) - 1
            # error_positions.append(i + error_position)

        decoded_bits += codeword[0] + codeword[1] + codeword[2] + codeword[4]  # Ignore parity bits

    # Correct the errors
    for position in error_positions:
        corrected_bit = '1' if output_bits[position] == '0' else '0'
        output_bits = output_bits[:position] + corrected_bit + output_bits[position + 1:]

    # Calculate Bit Error Rate (BER)
    total_errors = sum([int(a) != int(b) for a, b in zip("".join(encoded_bits), output_bits)])
    total_bits = len("".join(encoded_bits))
    BER = round(total_errors / total_bits, 20)

    return BER

