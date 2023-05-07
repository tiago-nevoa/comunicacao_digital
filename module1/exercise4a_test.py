from exercise4a import *

sequence = 'abcabcd'
constantKey = 3333333

cypherText = makeVernamCypher(sequence, constantKey)
print(f"CypherText in binary is:    {bin(cypherText)}")
decipherText = makeVernamCypher(cypherText, constantKey)
print(f"DecipherText in binary is:  {bin(decipherText)}")
print(f"The decipher message is:    {binaryToString(decipherText)}")
