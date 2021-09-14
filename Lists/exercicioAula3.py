def f_direita(direcao):
    direcao = direcao + 1
    if direcao == 4:
        direcao = 0
    return direcao


def f_esquerda(direcao):
    direcao = direcao - 1
    if direcao == -1:
        direcao = 3
    return direcao


def main():
    l = ["Norte", "Leste", "Sul", "Oeste"]
    l1 = ["D", "D", "D", "D", "E", "D", "E", "D", "E", "E", "D"]
    direcao = 0
    for i in l1:
        if i == "D":
            direcao = f_direita(direcao)
        else:
            direcao = f_esquerda(direcao)
    print(l[direcao])  # posso usar [] para pegar o elemento do indice


if __name__ == '__main__':
    main()
