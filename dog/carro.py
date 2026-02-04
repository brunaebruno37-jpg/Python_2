class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descricao_do_carro(self):
        nome_completo_do_carro = f'Carro {self.marca} {self.modelo} {self.ano}'
        return nome_completo_do_carro.title()
    
    def ler_odometro(self):
        print(f'Este carro tem {self.odometro} milhas no odômetro.')

    def atualizar_odometro(self,milenagem):
        if milenagem >= self.odometro:
            self.odometro = milenagem
        else:
            print("Você não pode reduzir a milhagem do odômetro!")

    def incrementar_odometro(self, milhas):
        self.odometro += milhas

    

meu_carro = Carro('mustang', 'GT', 2025)

'''print(meu_carro.descricao_do_carro())

meu_carro.atualizar_odometro(20)
meu_carro.atualizar_odometro(20)
meu_carro.atualizar_odometro(11)

meu_carro.ler_odometro()
meu_carro.atualizar_odometro(2)'''

class Battery():
    def __init__(self, battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-KWH battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message =  f'O carro pode ir aproximadamente {range} milhas com uma carga completa.'
        print(message)


class Eletrico(Carro):
    def __init__(self, marca, modelo,ano):
        super().__init__(marca, modelo,ano)
        self.battery = Battery()

    def describe_battery(self):
        print(f'A bateria desse carro tem {self.battery_size} KWH battery.')




my_tesla = Eletrico('Tesla', 'Model S', 2024)


my_tesla.battery.describe_battery()
print(my_tesla.descricao_do_carro())
my_tesla.battery.get_range()

