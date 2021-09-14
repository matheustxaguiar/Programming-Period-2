def buscaBin(x, l, esquerda, direita):
    if direita < esquerda:
        return -1

    meio = (esquerda+direita)//2

    if l[meio] == x:
        return f"Encontrei o número {x} na posição {meio}"
    if l[meio] >= x:
        direita = meio - 1
        return buscaBin(x, l, esquerda, direita)
    else:
        esquerda = meio + 1
        return buscaBin(x, l, esquerda, direita)


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 6
    esquerda = 0
    direita = len(l)-1
    resultado = buscaBin(x, l, esquerda, direita)
    print(l)
    print(resultado)


if __name__ == '__main__':
    main()
