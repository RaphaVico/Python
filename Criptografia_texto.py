def escolha():
    global key
    a = []
    item = []
    modo = input("D para decodificar e E para encripitar\n").lower()
    if modo == "d":
        string = input("Insira sua frase:\n")
        for i in string:
            a.append(ord(i))
        for x in a:
            item.append(chr(x+key))
        print(''.join(item))
        return main()
    if modo == 'e':
        string = input("Insira sua frase:\n")
        for i in string:
            a.append(ord(i))
        for x in a:
            item.append(chr(x - key))
        print(''.join(item))
        return main()
def rot():
    global key
    chave = int(input("Insira sua chave (1-127)\n"))
    if chave > 127:
        print("Valor não aceito\n")
        return rot()
    if chave < 1:
        print("Valor não aceito\n")
        return rot()
    key = chave
    return escolha()
def main():
    rot()
key = int
main()