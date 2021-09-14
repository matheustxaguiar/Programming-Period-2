def metade():
    lista = []
    for i in range(10):
        num = float(input("Insira um número: "))
        num = num / 2
        lista.append(num)
    print(lista)


if __name__ == "__main__":
    metade()
