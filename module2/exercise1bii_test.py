import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from module1.exercise5b_i import interleave, deinterleave
from exercise1bii import BER_repetition_code_bsc_correction_mode, count_bits_through_BSC, count_different_symbols

error_rates = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]
input_files = ["TestFilesCD/alice29.txt", "TestFilesCD/progc.c"]
interleaving_output_file = "interleaving_output.txt"
rows = 2 # for interleave
columns = 3 # for interleave

for file in input_files:
    with open(file, 'r') as input_file, open(interleaving_output_file, 'w') as output_file:
        data = input_file.read()
        interleaved_data = interleave(data, rows, columns)
        output_file.write(interleaved_data)

    print("--------------------")
    print(file)
    print("--------------------")
    bits_through_BSC = count_bits_through_BSC(interleaving_output_file, rows, columns)
    print("Number of bits through the BSC:", bits_through_BSC)
    print("--------------------")
    print("For each p in", error_rates)
    print()
    for error_rate in error_rates:
        BER = BER_repetition_code_bsc_correction_mode(interleaving_output_file, error_rate, 3, rows, columns)
        different_symbols = count_different_symbols(file, error_rate, rows, columns)
        print("p:", error_rate)
        print("BER:", BER)
        print("Number of different symbols:", different_symbols)
        print()