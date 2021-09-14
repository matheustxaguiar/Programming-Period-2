def sublista():
    l = []
    sublista = []
    for i in range(6):
        l.append(int(input("insira um valor a lista: ")))
    print(l)
    x = int(input("x: "))
    y = int(input("y: "))
    for j in range(x+1, y):
        for k in l:
            if k == j:
                sublista.append(k)
    print(f"Os elementos que comprrendem x e y e estão dentro da lista são: {sublista}")


if __name__ == '__main__':
    sublista()
