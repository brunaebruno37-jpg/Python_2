class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descricao_do_carro(self):
        nome_completo_do_carro = f'Carro {self.marca} {self.modelo} {self.ano}'
        return nome_completo_do_carro.title()
    
    def ler_odometro(self,milenage):
        print(f'Este carro tem {self.odometro} milhas no odômetro.')

    def atualizar_odometro(self,milenagem):
        self.odometro = milenagem
    

meu_carro = Carro('mustang', 'GT', 2025)

print(meu_carro.descricao_do_carro())
meu_carro.ler_odometro(14)
