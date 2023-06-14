from module1.exercise5b_i import interleave, deinterleave
from module1.exercise5a import binary_symmetric_channel
from module1.exercise4a import stringToBinary, binaryToString

def calculate_BER(file, error_rate, interleave_rows, interleaving_columns):
    with open(file, 'r') as f:
        contents = f.read()

    interleaved_contents = interleave(contents, interleave_rows, interleaving_columns)
    input_bits = "".join(interleaved_contents).replace("0b", "")
    output_bits = binary_symmetric_channel(input_bits, error_rate)

    results = [(ord(a) ^ ord(b)) for a, b in zip(input_bits, output_bits)]
    total_errors = len([num for num in results if num == 1])
    total_bits = len(list(output_bits))

    BER = round(total_errors / total_bits, 7)
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
