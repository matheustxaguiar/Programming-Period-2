def merge(l, esquerda, direita):
    i, j, k = 0, 0, 0  # i - lista esquerda, j - lista direta  e k - listona

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            l[k] = esquerda[i]
            i = i + 1
        else:
            l[k] = direita[j]
            j = j + 1
        k = k + 1

    while i < len(esquerda):
        l[k] = esquerda[i]
        i = i + 1
        k = k + 1

    while j < len(direita):
        l[k] = direita[j]
        j = j + 1
        k = k + 1



def mergeSort(l):
    if len(l) > 1:
        meio = len(l)//2
        esquerda = l[:meio]
        direita = l[meio:]

        mergeSort(esquerda)
        mergeSort(direita)


        merge(l, esquerda, direita)

    return l


def main():
    l = [3, 2, 1]
    print(mergeSort(l))


if __name__ == '__main__':
    main()
