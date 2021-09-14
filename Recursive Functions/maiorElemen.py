def maior(x, y):
    if x>y:
        return x
    else:
        return y


def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return maior(lista[0], maximo(lista[1:]))


def main():
    lista = [1, 2, 3, 4, 5, 6]
    resultado = maximo(lista)
    print(resultado)


if __name__ == '__main__':
    main()
