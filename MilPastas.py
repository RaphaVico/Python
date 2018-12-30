#Cria mil pastas e move um arquivo para uma dessas pastas

import os, random, shutil

path = os.getcwd()+'\\Mil Pastas'
for i in range(1,1001):
    pasta = 'Pasta %s' %i
    print('Criando', pasta)
    os.mkdir(path+'\\'+pasta) #Criando as pastas

num = str(random.randint(0,1000))
pasta_random = path+'\\Pasta '+ num
print('Movido para pasta:', pasta_random)
shutil.move('C:\\Users\\Rapha\\Desktop\\teste.txt', pasta_random) #movendo o arquivo
print('Done!')
