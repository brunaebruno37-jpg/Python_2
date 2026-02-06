arquivo = 'geste_book.txt'

while True:
    nome = input('Digite o seu nome:')

    if nome.lower() == 'sair':
        break
    
    print(f'Olá {nome}, seja bem-vindo(a)!')

    with open(arquivo, 'a') as file_object:
        file_object.write(f'Usuario: {nome}\n')
    print()
    
    motivo = input('Por qual motivo você estuda programacao:  ')

    with open(arquivo, 'a') as file_object:
        file_object.write(f'Motivo de estudar programacao: {motivo}\n')
    print()
