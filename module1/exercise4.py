# Considere a cifra de Vernam para ficheiros de texto. Esta cifra realiza o XOR bit a bit de todos os caracteres
# de duas sequências, plainText e theKey, resultando ainda uma sequência de caracteres, cipherText.

# (a) Implemente a função cypherText = makeVernamCypher(plainText, theKey), sendo os parâmetros de entrada
# e o valor de retorno, sequências de caracteres com a dimensão do texto em claro (plainText). Demonstre o (bom)
# funcionamento fazendo a cifra e a decifra da sequência abcabcd, considerando a chave constante e igual a 3333333.

def makeVernamCypher(plainText, theKey):
  # convert plainText to int
  if isinstance(plainText, str):
    plainText = stringToBinary(plainText)
  # plainText XOR theKey
  return plainText^theKey

def binaryToString(number):
  sequenceBytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')
  stringSequence = sequenceBytes.decode('UTF-8')
  return stringSequence

def stringToBinary(text):
  return int.from_bytes(text.encode(), "big")
  

# sequence = 'abcabcd'
# sequenceIntFormat = int.from_bytes(sequence.encode(), "big")
# print("Sequence in binary format is: " + bin(sequenceIntFormat))

# constantKey = 3333333
# print("Key in binary format is: " + bin(constantKey))

# cypherText = makeVernamCypher(sequence, constantKey)
# decypherText = makeVernamCypher(cypherText, constantKey)

# print("Is the decypher correct?")
# print(sequenceIntFormat==decypherText)
# print("Has the sequence returned to the original format?")
# print("Result: " + binaryToString(decypherText))


# (b) Realize a cifra do ficheiro alice29.txt (texto em claro) com a chave constante e com chave correspondendo a uma
# sequência aleatória de caracteres. Para ambas as situações determine os histogramas e entropias do texto em claro e do
# texto cifrado. Compare os resultados e comente.

alice_cypher = makeVernamCypher()

n = len(list(str(constantKey)))
chunks = []

with open(file, "r", errors='ignore') as f:
  lines = f.readlines()
  for line in lines:
    chunks.append([line[i:i+n] for i in range(0, len(line)), n)]))

print(chunks)
    