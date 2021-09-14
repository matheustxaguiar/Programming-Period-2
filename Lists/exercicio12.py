def temperaturas():
    n = int(input("n: "))
    temperatura = []
    cont = 0
    for i in range(n):
        temperatura.append(float(input("temperatura em °C: ")))
    media = sum(temperatura)/n
    print("A média da temperatura é: %.f" % media)
    for j in temperatura:
        if j < media:
            cont = cont + 1
    print(temperatura)
    print("A temperatura ficou abaixo da média %.f dias" % cont)


if __name__ == '__main__':
    temperaturas()
