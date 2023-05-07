from module1.exercise1d import *
from exercise3c import password_generator
from exercise4b import *


fileIn = "TestFilesCD/alice29.txt"
fileOutEnc = "Output_Files/encrypted_file.txt"
fileOutDec = "Output_Files/decrypted_file.txt"

# key generation
theKey = password_generator().encode('utf-8')
print("The generator key is: ")
print(theKey)

# cypher file
cypher_file(fileIn, fileOutEnc, theKey)
print("File Encrypted.. Done!")

# decipher_file
cypher_file(fileOutEnc, fileOutDec, theKey)
print("File Decrypted.. Done!")

# histograms and entropies
print("\nHistogram and Entropy...\n")
# plain text file
print(f'File: {fileIn}')
histogram(fileIn)
print("Entropy")
print(f'H = {round(entropy(fileIn), 2)}')
# cyphered file
print(f'File: {fileOutEnc}')
histogram(fileOutEnc)
print("Entropy")
print(f'H = {round(entropy(fileOutEnc), 2)}')
# deciphered file
print(f'File: {fileOutDec}')
histogram(fileOutDec)
print("Entropy")
print(f'H = {round(entropy(fileOutDec), 2)}')

