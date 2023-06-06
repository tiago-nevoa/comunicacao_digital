from exercise1ai import calculate_BER

error_rates = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]
list_of_files = ["TestFilesCD/a.txt", "TestFilesCD/alice29.txt", "TestFilesCD/cp.htm", "TestFilesCD/progc.c"]

for file in list_of_files:
    print(file)
    for error_rate in error_rates:
        BER = calculate_BER(file, error_rate)
        print("Error Rate:", error_rate)
        print("BER:", BER)
        print()
