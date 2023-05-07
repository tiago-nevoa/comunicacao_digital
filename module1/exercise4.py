from pathlib import Path
from exercise3 import password_generator

# Considere a cifra de Vernam para ficheiros de texto. Esta cifra realiza o XOR bit a bit de todos os caracteres
# de duas sequências, plainText e theKey, resultando ainda uma sequência de caracteres, cipherText.

# (a) Implemente a função cypherText = makeVernamCypher(plainText, theKey), sendo os parâmetros de entrada
# e o valor de retorno, sequências de caracteres com a dimensão do texto em claro (plainText). Demonstre o (bom)
# funcionamento fazendo a cifra e a decifra da sequência abcabcd, considerando a chave constante e igual a 3333333.

files_path = Path("TestFilesCD/")


def makeVernamCypher(plainText, theKey):
    # convert plainText to int
    if isinstance(plainText, str):
        plainText = stringToBinary(plainText)
    # plainText XOR theKey
    return plainText ^ theKey


def binaryToString(number):
    sequenceBytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')
    stringSequence = sequenceBytes.decode('UTF-8')
    return stringSequence


def stringToBinary(text):
    return int.from_bytes(text.encode(), "big")


def readFile(file, key):
    n = len(list(str(key)))

    with open(file, "r", errors='ignore') as f:
        text = f.read()
        chunks = [text[i:i + n] for i in range(0, len(text), n)]

    return chunks


def writeFile(file, contents):
    # Open the file in write mode
    with open(file, "w", errors='ignore') as file:
        # Write the modified contents back to the file
        file.write(contents)


sequence = 'abcabcd'
# sequenceIntFormat = int.from_bytes(sequence.encode(), "big")
# print("Sequence in binary format is: " + bin(sequenceIntFormat))

constantKey = 3333333
# print("Key in binary format is: " + bin(constantKey))

# cypherText = makeVernamCypher(sequence, constantKey)
# decypherText = makeVernamCypher(cypherText, constantKey)


# (b) Realize a cifra do ficheiro alice29.txt (texto em claro) com a chave constante e com chave correspondendo a uma
# sequência aleatória de caracteres. Para ambas as situações determine os histogramas e entropias do texto em claro e do
# texto cifrado. Compare os resultados e comente.

file = files_path / "alice29.txt"
# sequence_cypher = makeVernamCypher(sequence, constantKey)
# sequence_decipher = makeVernamCypher(sequence_cypher, constantKey)
# print(sequence_cypher)
# print(binaryToString(sequence_decipher))

# Cypher
chunks = readFile(file, constantKey)

chunksCyphered = []
for chunk in chunks:
    chunksCyphered.append(makeVernamCypher(chunk, constantKey))

chunksCypheredStrings = []
for chunk in chunksCyphered:
    chunksCypheredStrings.append(str(chunk))
chunksCypheredStrings = ''.join(chunksCypheredStrings)
writeFile("cypheredFile.txt", chunksCypheredStrings)

chunksDeciphered = []
for chunk in chunksCyphered:
    # chunksDeciphered.append(makeVernamCypher(chunk, constantKey))
    # print(len(str(makeVernamCypher(chunk, constantKey))))
    chunksDeciphered.append(binaryToString(makeVernamCypher(chunk, constantKey)))

print(''.join(chunksDeciphered))
chunksDeciphered = ''.join(chunksDeciphered)
writeFile("decipheredFile.txt", chunksDeciphered)

# chunksCyphered = ''.join(chunksCyphered)
#
# writeFile("cypheredFile.txt", chunksCyphered)
#
# #Decipher
# cypheredChunks = readFile("cypheredFile.txt", constantKey)
#
# chunksDeciphered = []
# for chunk in cypheredChunks:
#   # chunksDeciphered.append(binaryToString(makeVernamCypher(chunk, constantKey)))
#   # print(makeVernamCypher(chunk, constantKey), binaryToString(makeVernamCypher(chunk, constantKey)))
#
# chunksDeciphered = ''.join(chunksCyphered)
#
# writeFile("decipheredFile.txt", chunksDeciphered)

# VernamManiacs -------------------> Check this propose to exc 4.b

theKey = password_generator().encode('utf-8')
print(theKey)
fileIn = files_path / "alice29.txt"
fileOutEnc = files_path / "encrypted-file.txt"
fileOutDec = files_path / "decrypted-file.txt"


def cypher_file(input_file_name, output_file_name, key):
    with open(input_file_name, 'rb') as input_file, open(output_file_name, 'wb') as output_file:
        while True:
            byte_block = input_file.read(len(key))  # read a block of bytes from the input file
            if not byte_block:  # check if the end of the file is reached
                break
            xor_block = bytes(
                [b ^ k for b, k in zip(byte_block, key)])  # perform XOR operation with the corresponding key value
            output_file.write(xor_block)  # write the result to the output file


cypher_file(fileIn, fileOutEnc, theKey)

cypher_file(fileOutEnc, fileOutDec, theKey)
