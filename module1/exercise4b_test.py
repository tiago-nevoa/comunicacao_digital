#from exercise2a import self_information_and_entropy
from exercise3 import password_generator
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

