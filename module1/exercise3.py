import random
from random import randrange
import string

# (a) Implemente uma fonte de símbolos genérica, a qual gera ficheiros com N símbolos, de acordo com a Função Massa de
# Probabilidade (FMP) do alfabeto de M símbolos: p(x) = {p(x1), p(x2), . . . , p(xM)}.
# função recebe por ex um dicionário e.g: {'o': 1/2, 'a': 1/4, ...}, N
# M -> número de keys no dicionário

def generic_symbols_source(symb_map, n):

  letters = []

  for key, value in symb_map.items():
    array = list(int(n * value) * key)
    for elem in array:
      letters.append(elem)

  random.shuffle(letters)

  file = open("output.txt", "w")
  for letter in letters:
    file.write(letter)
  file.close()

# generic_symbols_source({'o': 1/4, 'a': 1/4, 'f': 1/8, 'e': 1/4, 'z': 1/8}, 3000)


# VERSION 2: GENERATE ANY RANDOM LIST OF ALL DIGIT
def generateFiles(numSymbols):

  chars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

  symbols = [] 

  for i in range(numSymbols):
      symbols.append(chars[random.randint(0,len(chars) - 1)])

  print(symbols)

  return symbols

#generateFiles(100)

# (b) Produza sequências com diferentes dimensões N, para valores de N à sua escolha. Compare o valor da entropia da fonte,
# H(X), com o valor estimado para a entropia das sequências geradas. Comente os resultados obtidos, em função do par
# de valores M e N.


# (c) Recorra à implementação da fonte de símbolos, para realizar um gerador de palavras-passe robustas, com dimensão entre
# 8 e 12 caracteres. Apresente cinco exemplos de palavras-passe geradas.

def password_generator():

  all_symbols = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

  password_size = randrange(8,13)
  random_symbols = random.choices(all_symbols, k=password_size)

  password = ''.join(random_symbols)
  return password


results = []

for num in range(5):
  results.append(password_generator())

print(results)
    