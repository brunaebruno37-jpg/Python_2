import unittest
from cidade_pais import localizacao

class TestLocalizacao(unittest.TestCase):
    def teste_localizacao(self):
        resultado = localizacao('São Paulo', 'Brasil', '3 milhões')
        self.assertEqual(resultado, 'São Paulo Brasil 3 milhões')

unittest.main()