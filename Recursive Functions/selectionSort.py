def selectionSort(l):
    for i in range(len(l)):
        posmenor = i
        for j in range(i+1, len(l)):
            if l[posmenor] > l[j]:
                posmenor = j
        l[i], l[posmenor] = l[posmenor], l[i]
    return l


def main():
    l = [3, 2, 1, 4, 9, 10, 2, 3]
    print(l)
    resultado = selectionSort(l)
    print(resultado)


if __name__ == '__main__':
    main()
