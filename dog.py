class Dog():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def sit(self):
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        print(f'{self.name.title()} rolled over! ')

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

'''print(f'my dog name is {my_dog.name.title()}.')
print(f'a idade do meu cachorro é {my_dog.age}.')
my_dog.sit()
my_dog.roll_over()

print(f'nome do seu cachorro é {your_dog.name.title()}.')
print(f'a idade do seu cachorro é {your_dog.age}.')
your_dog.sit()'''

class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numero_de_clientes = 0

    def describe_restaurant(self):
        print(f' o nome do restaurante é {self.restaurant_name.title()}')
        print(f' o tipo culinário é  {self.cuisine_type.title()}')

    def open_restaurant(self):
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')

    def number_served(self, numero_de_clientes):
        self.numero_de_clientes = numero_de_clientes
        print(f'Numero de clientes atendidos: {self.numero_de_clientes}')

    def set_number_served(self, numero_de_clientes):
        self.numero_de_clientes += numero_de_clientes
        print(f'Numero de clientes atendidos: {self.numero_de_clientes}')
    
    def numero_total_de_atendimentos(self):
        print(f'Numero total de atendimentos: {self.numero_de_clientes}')


restaurant = Restaurante('Sabor do nordeste', 'comida tipica')
'''restaurant.number_served(30)
restaurant.set_number_served(20)
restaurant.set_number_served(20)'''


'''restaurant.describe_restaurant()
restaurant.open_restaurant()'''

class User():
    def __init__(self, primeiro_nome, segundo_nome, idiade, cidade):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.idade = idiade
        self.cidade = cidade
        self.tentaivas_de_login = 0

    def total_tentativas_de_login(self, tentativas):
        self.tentaivas_de_login += tentativas
        print(f'Tentativas de login: {self.tentaivas_de_login}')

    def resetar_tentativas_de_login(self):
        self.tentaivas_de_login = 0
        print('Tentativas de login retadas para 0.')


    def descricao_usuario(self):
        print(f'Seu nome é {self.primeiro_nome.title()}')        
        print(f'Seu nome do meio é {self.segundo_nome.title()}')        
        print(f'Sua idade {self.idade}')        
        print(f'Mora em {self.cidade.title()}')     

    def saudacao_usuario(self):
        print(f'Seja bem vindo(a) {self.primeiro_nome.title()} {self.segundo_nome.title()}!')  


'''usuario3 = User('Bruno', 'Moreira', '29', 'Russas')
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.resetar_tentativas_de_login()
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)
usuario3.total_tentativas_de_login(1)'''


'''usuario = User('Bruno', 'Moreira', '29', 'Russas')
usuario2 = User('bruna', 'Rodrigues', '25', 'Russas')

usuario.descricao_usuario()
usuario.saudacao_usuario()

usuario2.descricao_usuario()
usuario2.saudacao_usuario()'''