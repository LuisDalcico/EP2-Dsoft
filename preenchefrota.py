import defineposicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    
    return frota