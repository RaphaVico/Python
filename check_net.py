import urllib3

def main():
    print(check)

if __name__ == '__main__':
    try:
        host = urllib3.PoolManager()
        r = host.request('GET', 'www.google.com')
        check = 'Conectado'
    except:
        check = 'Desconectado'
    if check == 'Conectado':
        main()
    else:
        print(check)
