
with open('Python.txt') as file_object:
    content = file_object.read()
   
for line in range(3):
    print(content)

print()
mensagem = content
mensagem = mensagem.replace('arquivos','Progamas em segundo plano')
print(mensagem)
