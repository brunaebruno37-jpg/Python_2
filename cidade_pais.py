
def localizacao(cidade, pais, populacao=''):
    informacoes = f'{cidade.title()} {pais.title()}'
    if populacao:
        informacoes = f'{cidade.title()} {pais.title()} {populacao}'
    return informacoes
