'''with open('trabalho\pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)'''



filename =  'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))