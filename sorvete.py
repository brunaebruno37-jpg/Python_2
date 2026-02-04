
from dog import Restaurante
from dog import User





class Privileges():
    def privileges(self):
        privilegios = ['can add post', 'can delete post', 'can ban user']
        print(f'Os privilégios do administrador são: {privilegios}')
    

class Admin(User, Privileges):
    def __init__(self, primeiro_nome, segundo_nome, idiade, cidade):
        super().__init__(primeiro_nome, segundo_nome, idiade, cidade)

class IceCreamStand(Restaurante):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def flavors(self):
        sabores = ['chocolate', 'baunilha', 'morango', 'flocos', 'napolitano']
        print(f'Os sabores disponívei são: {sabores}')

sabores_disponiveis = IceCreamStand('Gelado do nordeste', 'sorvetes')
admin = Admin('Bruna', 'Roddrigues', 25, 'Russas')
privilegios = Privileges()


sabores_disponiveis.flavors()
print()
admin.privileges()
print()
admin.descricao_usuario()
print('teste')
print('teste2')
    