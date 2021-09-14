def fibonacci(n):
    ult = 0
    penult = 1
    lista = [1]
    if n == 1:
        lista = [1]
    if n == 2:
        lista = [1, 1]
    if n > 2:
        for i in range(n):
            soma = ult + penult
            lista.append(soma)
            ult = penult
            penult = soma
        lista.pop()
    return lista


def main():
    n = int(input("n: "))
    sequencia = fibonacci(n)
    print(sequencia)


if __name__ == '__main__':
    main()
