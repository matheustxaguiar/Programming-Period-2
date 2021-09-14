def main():
    lista = []
    for i in range(1, 100):
        if i % 2 == 0:
            lista.append(i)
    lista.reverse()
    print(lista)


if __name__ == "__main__":
    main()
