from exercise1aiii import BER_hamming_code_bsc_correction_mode

error_rates = [pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4), pow(10,-5)]
list_of_files = ["TestFilesCD/a.txt", "TestFilesCD/alice29.txt", "TestFilesCD/cp.htm", "TestFilesCD/Person.java","TestFilesCD/progc.c"]

# for file in list_of_files:
#     for error_rate in error_rates:
#         BER = repetition_code_bsc_correction_mode(file, error_rate)
#         print("Error Rate:", error_rate)
#         print("BER:", BER)
#         print()

test_file = list_of_files[1]
for error_rate in error_rates:
    print(test_file)
    BER = BER_hamming_code_bsc_correction_mode(test_file, error_rate)
    print("Error Rate:", error_rate)
    print("BER:", BER)
    print()

# for file in list_of_files:
#     print("-------------------------")
#     print(file)
#     print("-------------------------")
#     bits_through_BSC = count_bits_through_BSC(file, repetition_code=3)
#     print("Number of bits through the BSC:", bits_through_BSC)
#     print("For each p in", error_rates)
#     print()
#     for error_rate in error_rates:
#         BER = BER_repetition_code_bsc_correction_mode(file, error_rate, repetition_code=3)
#         different_symbols = count_different_symbols(file, error_rate)
#         print("p:", error_rate)
#         print("BER:", BER)
#         print("Number of different symbols:", different_symbols)
#         print()