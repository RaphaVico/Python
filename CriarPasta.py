import os


#Função para criar pasta 
def criar_pasta(directory):
    if os.path.exists(directory):
        print('Pasta já existe!')
    if not os.path.exists(directory):
        print('Criando pasta  ' + directory)
        os.makedirs(directory)
    

criar_pasta('Nome da Pasta')
