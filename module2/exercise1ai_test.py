from exercise1ai import calculate_BER, count_bits_through_BSC, count_different_symbols

error_rates = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]
list_of_files = ["TestFilesCD/alice29.txt", "TestFilesCD/cp.htm", "TestFilesCD/Person.java","TestFilesCD/progc.c"]
# list_of_files = ["TestFilesCD/a.txt"]

for file in list_of_files:
    print("-------------------------")
    print(file)
    print("-------------------------")
    bits_through_BSC = count_bits_through_BSC(file)
    print("Number of bits through the BSC:", bits_through_BSC)
    print("For each p in", error_rates)
    print()
    for error_rate in error_rates:
        BER = calculate_BER(file, error_rate)
        different_symbols = count_different_symbols(file, error_rate)
        print("p:", error_rate)
        print("BER:", BER)
        print("Number of different symbols:", different_symbols)
        print()


