def define_posicoes(linha, coluna, orientacao, tamanho):
    indice = 0
    grid = []
    if orientacao == 'horizontal':
        while indice < tamanho:
            grid.append([linha, coluna + indice])
            indice += 1
    elif orientacao == 'vertical':
        while indice < tamanho:
            grid.append([linha + indice, coluna])
            indice += 1
    return grid


def preenche_frota(dicionario_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in dicionario_frota:
        dicionario_frota[nome_navio] = []
    dicionario_frota[nome_navio].append(posicoes)
    return dicionario_frota


def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro 