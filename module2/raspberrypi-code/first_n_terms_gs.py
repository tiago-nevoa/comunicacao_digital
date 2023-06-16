# (a) Função que apresenta os primeiros N termos da progressão geométrica de primeiro termo u e razão r.
# Os valores de N, u e r são passados como parâmetro.

def first_n_terms_gs(u, r, N, error_check):
    terms = [u]
    for num in range(1,N):
        term = u * r**num
        terms.append(term)
    return terms