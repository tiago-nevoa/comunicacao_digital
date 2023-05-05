# Considere a cifra de Vernam para ficheiros de texto. Esta cifra realiza o XOR bit a bit de todos os caracteres
# de duas sequências, plainText e theKey, resultando ainda uma sequência de caracteres, cipherText.

# (a) Implemente a função cypherText = makeVernamCypher(plainText, theKey), sendo os parâmetros de entrada
# e o valor de retorno, sequências de caracteres com a dimensão do texto em claro (plainText). Demonstre o (bom)
# funcionamento fazendo a cifra e a decifra da sequência abcabcd, considerando a chave constante e igual a 3333333.

def makeVernamCypher(plainText, theKey):

  if isinstance(plainText, int):
    return bin(plainText^theKey)
  else:
    numbers = []

    binary_sequence = ''.join(format(ord(x), 'b') for x in plainText)
    
    value = bin(int(binary_sequence, 2)^theKey)

    return isinstance(value, str)
    
sequence = 'abcabcd'
constantKey = 3333333

cypherText = makeVernamCypher(sequence, constantKey)

decypherText = makeVernamCypher(cypherText, constantKey)

print(cypherText)
# print("********************************")
print(decypherText)

# (b) Realize a cifra do ficheiro alice29.txt (texto em claro) com a chave constante e com chave correspondendo a uma
# sequência aleatória de caracteres. Para ambas as situações determine os histogramas e entropias do texto em claro e do
# texto cifrado. Compare os resultados e comente.