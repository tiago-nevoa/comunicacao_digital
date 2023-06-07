from exercise1aii import repetition_code_bsc_correction_mode

error_rates = [pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4), pow(10,-5)]
list_of_files = ["TestFilesCD/a.txt", "TestFilesCD/alice29.txt", "TestFilesCD/cp.htm", "TestFilesCD/progc.c"]

# for file in list_of_files:
#     for error_rate in error_rates:
#         BER = repetition_code_bsc_correction_mode(file, error_rate)
#         print("Error Rate:", error_rate)
#         print("BER:", BER)
#         print()

test_file = list_of_files[1]
for error_rate in error_rates:
    print(test_file)
    BER = repetition_code_bsc_correction_mode(test_file, error_rate)
    print("Error Rate:", error_rate)
    print("BER:", BER)
    print()