def maior(lista):
    m = 0
    for j in lista:
        if j > m:
            m = j
    return m


def posicao_do_max():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 2, 7]
    print(lista)
    ma = maior(lista)
    for i in lista:
        if i == ma:
            indice = lista.index(i)
            print(f"O maior indice do maior valor da lista é: {indice}")


if __name__ == '__main__':
    posicao_do_max()
