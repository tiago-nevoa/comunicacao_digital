def calculate_fletcher_checksum(data):
    # initialize sum1 and sum2 to zero
    sum1 = sum2 = 0
    # for each byte in the data
    for byte in data:
    # add it to sum1 and update sum2 by adding the current value of sum1 
    # sum1 and sum2 are reduced modulo 255 to keep them within the valid range
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    # the final values of sum1 and sum2 represent the checksum
    # to get one checksum value: sum2 is shifted left by 8 bits and is combined with sum1 using an OR operation
    checksum = (sum2 << 8) | sum1
    return checksum

# verify the integrity of the data using the fletcher checksum
def verify_fletcher_checksum(data, checksum):
    # recalculate the checksum of the received data using the same algorithm
    calculated_checksum = calculate_fletcher_checksum(data)
    # compare the recalculated checksum with the received checksum
    # if they match, the data was successfully transmitted
    # else an error has occurred during transmission
    return calculated_checksum == checksum


# ***************************************************************************************
# Relatório:
# The Fletcher checksum algorithm is a simple method that can detect most single-bit errors 
# and some burst errors. However, it is not foolproof and may not detect all errors. 
# It's important to note that the Fletcher checksum is not designed for error correction 
# but rather for error detection. If error correction is required, more sophisticated techniques 
# such as error-correcting codes like Reed-Solomon or Hamming codes should be considered.