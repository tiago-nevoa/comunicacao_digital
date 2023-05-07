from exercise5a import binary_symmetric_channel
from exercise4a import stringToBinary

# transmitted_bits = binary_symmetric_channel("01001", 0.6)

# print(transmitted_bits)
binary_file_sequence = []

with open('alice29.txt', 'r') as f:
    contents = f.readlines()
    for line in contents:
        binary_file_sequence.append(bin(stringToBinary(line)))
f.close()

binary_file_sequence = "".join(binary_file_sequence).replace("0b", "")
transmitted_bits = binary_symmetric_channel(binary_file_sequence, 0.6)

print(transmitted_bits)