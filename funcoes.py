def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):

    grid = [[0 for i in range(10)] for i in range(10)]

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha, coluna = posicao
                grid[linha][coluna] = 1 
    return grid 

def afundados(frota, tabuleiro):
    afund = 0

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            afundado = True
            for posicao in navio:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado:
                afund = afund + 1

    return afund
 

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
        else:
            posicoes.append([linha + i, coluna])
    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    nov_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for pos in nov_posicoes:
        linha, coluna = pos
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for pos in navio:
                if pos in nov_posicoes:
                    return False

    return True


