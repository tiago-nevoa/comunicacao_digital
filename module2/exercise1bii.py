import sys
import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5b_i import interleave, deinterleave
from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary, binaryToString

def BER_repetition_code_bsc_correction_mode(file, error_rate, repetition_code, interleaving_rows, interleaving_columns):
  with open(file, 'r') as f:
      contents = f.read()

  interleaved_contents = interleave(contents, interleaving_rows, interleaving_columns)

  input_bits=bin(stringToBinary(interleaved_contents)).replace("0b","")
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


def count_bits_through_BSC(file, interleaving_rows, interleaving_columns):
    with open(file, 'rb') as f:
        contents = f.read()
        interleaved_contents = interleave(contents, interleaving_rows, interleaving_columns)
        file_bits = len(interleaved_contents) * 8  # *8 because Python reads file in bytes
    return file_bits


def count_different_symbols(file, error_rate, interleaving_rows, interleaving_columns):
    with open(file, 'r') as f:
        chars_A = f.read()
    f.close()

    chars_A_bin = bin(stringToBinary(chars_A))[2:]
    chars_B_bin = binary_symmetric_channel(chars_A_bin, error_rate)
    chars_B = binaryToString(int(chars_B_bin, 2))  # Convert chars_B_bin to an integer
    chars_B_deinterleaved = deinterleave(chars_B,interleaving_rows, interleaving_columns)

    different_chars = 0
    for charA, charB in zip(chars_A, chars_B_deinterleaved):
        if charA != charB:
            different_chars += 1

    return different_chars