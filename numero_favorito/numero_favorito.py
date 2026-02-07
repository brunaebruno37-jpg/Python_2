import json

def numero_favorito():
    filenum = 'numero_user.json'
    try:
        with open(filenum, 'r') as f_obj:
            return json.load(f_obj)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def ler_numero_favorito():
    num_favorito = numero_favorito()
    
    if num_favorito:
        print(f'Bem-vindo de volta! Seu numero favorito é {num_favorito}')
    else:
        num_f = input('Digite o seu numero favorito: ')
        filenum = 'numero_user.json'
        with open(filenum, 'w') as f_obj:
            
            json.dump(num_f, f_obj)
        print(f'Não sabia que seu numero favorito era {num_f}!')

ler_numero_favorito()
