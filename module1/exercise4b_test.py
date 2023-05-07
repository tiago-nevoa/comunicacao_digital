from module1.exercise1d import *
from exercise3c import password_generator
from exercise4b import *


fileIn = "TestFilesCD/alice29.txt"
fileOutEnc = "Output_Files/encrypted_file.txt"
fileOutDec = "Output_Files/decrypted_file.txt"

theKey = password_generator().encode('utf-8')
print("The generator key is: ")
print(theKey)

cypher_file(fileIn, fileOutEnc, theKey)
print("File Encrypted.. Done!")

cypher_file(fileOutEnc, fileOutDec, theKey)
print("File Decrypted.. Done!")

print("\nSelf Information and Entropy...\n")
print(f'File: {fileIn}')
histogram(fileIn)
print("Entropy")
print(f'H = {round(entropy(fileIn), 2)}')

print(f'File: {fileOutEnc}')
histogram(fileOutEnc)
print("Entropy")
print(f'H = {round(entropy(fileOutEnc), 2)}')

print(f'File: {fileOutDec}')
histogram(fileOutDec)
print("Entropy")
print(f'H = {round(entropy(fileOutDec), 2)}')

