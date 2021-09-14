def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(origem, "->", destino)
    else:
        hanoi(n-1, origem, auxiliar, destino)
        print(origem, "->", destino)
        hanoi(n-1, auxiliar, destino, origem)


def main():
    hanoi(45, "A", "B", "C")


if __name__ == '__main__':
    main()
 