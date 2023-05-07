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

generic_symbols_source({'a': 1/2, 'b': 1/4, 'c': 1/8, 'd': 1/8}, 12)

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


five_strong_passwords = []

for num in range(5):
  five_strong_passwords.append(password_generator())

# print(five_strong_passwords)
    