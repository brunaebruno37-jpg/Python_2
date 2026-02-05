'''with open('trabalho\pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)'''



filename =  'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('Muito bom!')
print('Eu te amo Deus!')