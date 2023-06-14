from module1.exercise5b_i import interleave, deinterleave
from exercise1bi import calculate_BER, count_bits_through_BSC, count_different_symbols

error_rates = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]
input_files = ["TestFilesCD/a.txt", "TestFilesCD/alice29.txt", "TestFilesCD/cp.htm", "TestFilesCD/progc.c"]
interleaving_output_file = "interleaving_output.txt"
rows = 2 # for interleave
columns = 3 # for interleave

for file in input_files:
    with open(file, 'r') as input_file, open(interleaving_output_file, 'w') as output_file:
        data = input_file.read()
        interleaved_data = interleave(data, rows, columns)
        output_file.write(interleaved_data)

    deinterleaved_data = deinterleave(interleaved_data, rows, columns)
    print("--------------------")
    print(file)
    print("--------------------")
    bits_through_BSC = count_bits_through_BSC(interleaving_output_file, rows, columns)
    print("Number of bits through the BSC:", bits_through_BSC)
    print("--------------------")
    print("For each p in", error_rates)
    print()
    for error_rate in error_rates:
        BER = calculate_BER(interleaving_output_file, error_rate, rows, columns)
        different_symbols = count_different_symbols(file, error_rate, rows, columns)
        print("p:", error_rate)
        print("BER:", BER)
        print("Number of different symbols:", different_symbols)
        print()