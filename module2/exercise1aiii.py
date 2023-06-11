import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary

# (ii) BER3, após a aplicação de código de Hamming (7, 4) sobre o BSC, em modo de correção;

def hamming_code_bsc_correction_mode(file, error_rate):
    input_bits = []

    with open(file, 'r') as f:
        contents = f.readlines()
        for line in contents:
            input_bits.extend(bin(stringToBinary(line)).replace("0b", "").zfill(4))
    f.close()

    encoded_bits = []  # Initialize encoded_bits as a list

    # Encode the input bits using Hamming (7, 4) code
    for i in range(0, len(input_bits), 4):
        # Check if there are enough bits remaining to form a complete group
        if i + 4 > len(input_bits):
            break

        message = input_bits[i:i + 4]

        # Calculate parity bits
        parity_1 = str((int(message[0]) + int(message[1]) + int(message[3])) % 2)
        parity_2 = str((int(message[0]) + int(message[2]) + int(message[3])) % 2)
        parity_3 = str((int(message[1]) + int(message[2]) + int(message[3])) % 2)

        # Construct the encoded bits
        encoded_bits += message + [parity_1, parity_2, parity_3]  # Append to the list

    output_bits = binary_symmetric_channel("".join(encoded_bits), error_rate)

    decoded_bits = ''
    error_positions = []

    # Decode the received bits
    for i in range(0, len(output_bits), 7):
        # Check if there are enough bits remaining to form a complete group
        if i + 7 > len(output_bits):
            break

        codeword = output_bits[i:i + 7]

        # Calculate syndrome bits
        syndrome_1 = str((int(codeword[0]) + int(codeword[2]) + int(codeword[4]) + int(codeword[6])) % 2)
        syndrome_2 = str((int(codeword[1]) + int(codeword[2]) + int(codeword[4]) + int(codeword[5])) % 2)
        syndrome_3 = str((int(codeword[3]) + int(codeword[4]) + int(codeword[5]) + int(codeword[6])) % 2)

        # Check if any error occurred
        if int(syndrome_3 + syndrome_2 + syndrome_1, 2) != 0:
            # Error detected, find the position of the error
            error_position = int(syndrome_3 + syndrome_2 + syndrome_1, 2) - 1
            error_positions.append(i + error_position)

        decoded_bits += codeword[0] + codeword[1] + codeword[2] + codeword[4]  # Ignore parity bits

    # Correct the errors
    for position in error_positions:
        output_bits = output_bits[:position] + str(1 - int(output_bits[position])) + output_bits[position + 1:]

    # Calculate Bit Error Rate (BER)
    total_errors = sum([int(a) != int(b) for a, b in zip("".join(encoded_bits), output_bits)])
    total_bits = len("".join(encoded_bits))
    BER = round(total_errors / total_bits, 4)

    return BER



