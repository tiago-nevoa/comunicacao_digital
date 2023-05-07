
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
    return plainText ^ theKey


def stringToBinary(text):
    return int.from_bytes(text.encode(), "big")


def binaryToString(number):
    sequenceBytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')
    stringSequence = sequenceBytes.decode('UTF-8')
    return stringSequence


