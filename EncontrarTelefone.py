
import re
file = open('texto.txt', 'r')
telefone = re.compile(r'''(
(\d{4}|\(\d{4}\))? #codigo de area
(\s|-|\.)? #separador
(\d{5}|\d{4}) #primeiros digitos
(\s|-|\.)? #separador
(\d{4}) #ultimos digitos
)''', re.VERBOSE)
resultados = []
for line in file:
    for groups in telefone.findall(line):
        numero = ''.join([groups[1], groups[3], groups[5]])
        resultados.append(numero)
print('Os numeros de telefones encontrados são: ', resultados)
file.close()
