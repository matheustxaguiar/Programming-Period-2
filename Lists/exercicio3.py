def leitura():
    n = int(input("n: "))
    lista = []
    for i in range(n):
        num = int(input("Insira um número inteiro: "))
        lista.append(num)
    print(lista)


if __name__ == '__main__':
    leitura()
