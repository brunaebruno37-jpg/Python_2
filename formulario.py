user_name = input('Nome: ')

formulario_file = 'formulario.txt'

with open(formulario_file, 'w') as formulario_file:
    formulario_file.write(f'Nome: {user_name}.\n')
