def pot(numero, potencia):
    if potencia == 0:
        return 1
    else:
        return numero * pot(numero, potencia-1)


def main():
    num = int(input("Numero: "))
    potencia = int(input("Potencia: "))
    resultado = pot(num, potencia)
    print(resultado)


if __name__ == '__main__':
    main()
