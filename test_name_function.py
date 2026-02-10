import unittest

def name_function(pri_nome, segundo_nome,nome_meio=''):
    nome_completo = f'{pri_nome} {segundo_nome}'
    if nome_meio:
        nome_completo = f'{pri_nome} {segundo_nome} {nome_meio}'
    return nome_completo.title()

class NameTestCase(unittest.TestCase):
    def teste_fist_last_name(self):
        formatted_name = name_function('Jhon', 'Doe', 'Miller')
        self.assertEqual(formatted_name, 'Jhon Doe Miller')

unittest.main()

nome = name_function('Jhon', 'Doe')
#print(nome)
    