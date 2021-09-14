def buscaBin(x, l):
    esquerda = 0
    direita = len(l)-1
    while esquerda <= direita:
        meio = (esquerda+direita) // 2  # pega a posição do meio
        if l[meio] == x:
            return f"encontreio o {x} na posição {meio}"
        elif l[meio] > x:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    x = 6
    resultado = buscaBin(x, l)
    print(l)
    print(resultado)


if __name__ == '__main__':
    main()
