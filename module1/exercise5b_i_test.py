from exercise5b_i import *

print("Original data:")
print('abcdefg')

interleaved_data = interleave('abcdefg', 2, 3)

print("Data interleaved:")
print(interleaved_data)

deinterleaved_data = deinterleave(interleaved_data, 2, 3)

print("Data deinterleaved:")
print(deinterleaved_data)

