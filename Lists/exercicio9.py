def ordenadas_e_abscissas():
    abscissas = []
    ordenadas = []
    pares = 0
    impares = 0
    soma = 0
    produto = 1
    n = int(input("n: "))
    for i in range(n):
        abscissas.append(int(input("abscissa: ")))
        ordenadas.append(int(input("ordenadas: ")))
    print(abscissas)
    print(ordenadas)
    for j in abscissas:
        if j % 2 == 0:
            pares = pares + 1
    for k in ordenadas:
        if k % 2 != 0:
            impares = impares + 1
    if pares > impares:
        for y in abscissas:
            soma = soma + y
        print(f"A soma das abscissas é: {soma}")
    else:
        for p in ordenadas:
            produto = produto * p
        print(f"O produto das ordenadas é: {produto}")


if __name__ == '__main__':
    ordenadas_e_abscissas()
