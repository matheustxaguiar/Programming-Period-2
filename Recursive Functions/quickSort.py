def particao(l, inf, sup):
    pivot = l[inf]
    i = inf+1
    j = sup

    while i <= j:
        while i <= j and l[i] <= pivot:
            i = i + 1
        while j >= i and l[j] > pivot:
            j = j - 1
        if i < j:
            l[i], l[j] = l[j], l[i]

    l[inf], l[j] = l[j], l[inf]
    return j


def quickSort(l, inf, sup):
    if inf < sup:
        pos = particao(l, inf, sup)
        quickSort(l, inf, pos-1)
        quickSort(l, pos + 1, sup)
    return l


def main():
    l = [6, 5, 4, 3, 2, 1]
    resultado = quickSort(l, 0, len(l)-1)
    print(resultado)


if __name__ == '__main__':
    main()
