# (a) Implemente uma fonte de símbolos genérica, a qual gera ficheiros com N símbolos, de acordo com a Função Massa de
# Probabilidade (FMP) do alfabeto de M símbolos: p(x) = {p(x1), p(x2), . . . , p(xM)}.

# função recebe por ex um dicionário e.g: {'o': 1/2, 'a': 1/4, ...}, N
# M -> número de keys no dicionário

# values = [0,1]

# for num in range(1,100):
#   print(random.sample(values,1)[0])

def generic_symbols_source(symb_map, n):
  # probabilities array of symb_map
  probabilities = list(symb_map.values())

  for num in range(0,1):
    print(random.sample(probabilities,1))

  selected = 
  

# (b) Produza sequências com diferentes dimensões N, para valores de N à sua escolha. Compare o valor da entropia da fonte,
# H(X), com o valor estimado para a entropia das sequências geradas. Comente os resultados obtidos, em função do par
# de valores M e N.


# (c) Recorra à implementação da fonte de símbolos, para realizar um gerador de palavras-passe robustas, com dimensão entre
# 8 e 12 caracteres. Apresente cinco exemplos de palavras-passe geradas.