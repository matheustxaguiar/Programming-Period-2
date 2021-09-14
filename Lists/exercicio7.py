def inverter():
    lista = []
    invert = []
    cont = 1
    for i in range(10):
        lista.append(i)
    print(lista)
    while cont < len(lista) + 1:
        item = lista.index(len(lista) - cont)
        invert.append(item)
        cont = cont + 1
    print(invert)


if __name__ == '__main__':
    inverter()
