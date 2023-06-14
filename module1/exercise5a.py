import random

# binary_sequence -> input bits (0's and 1's) to transmit
# p -> probability of introducing an error (BER)
# returns a list of transmitted bits after potentially being flipped with probability p
def binary_symmetric_channel(binary_sequence, p):
  transmitted_bits = []

  for input_bit in binary_sequence:
    if input_bit == '0' or input_bit == '1':
      if random.random() < p:
        transmitted_bits.append(str(1 - int(input_bit)))
      else:
        transmitted_bits.append(input_bit)
    else:
      transmitted_bits.append(input_bit)

  return "".join(transmitted_bits)




