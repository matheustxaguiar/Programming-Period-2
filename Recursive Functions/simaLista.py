def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])


def main():
    lista = [1, 2, 3, 4, 5, 6]
    total = soma(lista)
    print(total)


if __name__ == '__main__':
    main()
