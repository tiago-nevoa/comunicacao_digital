import random

# binary_sequence -> input bits (0's and 1's) to transmit
# p -> probability of introducing an error (BER)
# returns a list of transmitted bits after potentially being flipped with probability p
def binary_symmetric_channel(binary_sequence, p):

  sequence_list = list(binary_sequence)

  output_bits = []

  for input_bit in sequence_list:
    if random.random() < p:
      # flip the input bit with probability p
      output_bits.append(1 - int(input_bit))
    else:
      # return the input bit unchanged
      output_bits.append(int(input_bit))

  return output_bits


