import requests 
import os 
import platform
from termcolor import*

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


systema = platform.system().lower
if systema == 'linux':
    os.system('clear')
elif systema== 'windows':
    os.system('cls')

url = str(input('Site para encontrar diretorios:'))
diretorios = ['admin','admin.php','login','login.php','sql','sql.sql','database','phpadmin','phpMyAdmin','senhas.txt','senhas.php','password','pass.txt','logins']
for brute_force in diretorios:
    novo_link = 'http://'+url+'/'+brute_force
    r = requests.get(novo_link)
    verific = r.status_code
    if verific == 404:
        print(bcolors.FAIL + 'Não encontrado', novo_link)
    else:
        print(bcolors.OKGREEN + 'Diretorio encontrado', novo_link)
