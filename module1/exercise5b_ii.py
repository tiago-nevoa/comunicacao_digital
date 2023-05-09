from exercise5b_i import *
from exercise5a import binary_symmetric_channel
from exercise4a import *

input_file = 'TestFilesCD/example.txt'
error_rate = 0
rows = 9
cols = 10

# Open the file in read mode
with open(input_file, 'r') as f:
    # Read the contents of the file as a string
    content = f.read()
    # Interleave the input data
    interleaved_data = interleave(content, rows, cols)

# Convert the interleaved data to a binary string
binary_data = ''.join(format(ord(char), '08b') for char in interleaved_data)

# Pass the binary data through the Binary Symmetric Channel (BSC)
received_binary_data = binary_symmetric_channel(binary_data, error_rate)

# Convert the received binary data back to a string
received_data = ''.join(chr(int(received_binary_data[i:i+8], 2)) for i in range(0, len(received_binary_data), 8))

# Deinterleave the input data
deinterleaved_data = deinterleave(received_data, rows, cols)

print(deinterleaved_data)



