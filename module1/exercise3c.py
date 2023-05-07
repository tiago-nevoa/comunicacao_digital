import random
from random import randrange
import string


# (c) Recorra à implementação da fonte de símbolos, para realizar um gerador de palavras-passe robustas, com dimensão entre
# 8 e 12 caracteres. Apresente cinco exemplos de palavras-passe geradas.

def password_generator():
    all_symbols = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

    password_size = randrange(8, 13)
    random_symbols = random.choices(all_symbols, k=password_size)

    password = ''.join(random_symbols)
    return password
