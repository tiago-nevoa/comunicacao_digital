from exercise5a import binary_symmetric_channel
from exercise4a import stringToBinary
from exercise4a import makeVernamCypher

input_bits = []
error_rate = 0.6

with open('alice29.txt', 'r') as f:
    contents = f.readlines()
    for line in contents:
        input_bits.append(bin(stringToBinary(line)))
f.close()

input_bits = "".join(input_bits).replace("0b", "")
output_bits = binary_symmetric_channel(input_bits, error_rate)

results = [(ord(a) ^ ord(b)) for a, b in zip(input_bits, output_bits)]

total_errors = len([num for num in results if num == 1])
total_bits = len(list(output_bits))

BER = round(total_errors / total_bits, 4)

