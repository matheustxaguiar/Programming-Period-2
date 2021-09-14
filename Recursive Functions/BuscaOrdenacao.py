def anterior(x, y, nomes):
    x1 , x2, x3 = x
    y1, y2, y3 = y


    if nomes[x1] < nomes[y1]:
        return True
    if nomes[x1] > nomes[y1]:
        return False

    if x2 > y2:
        return True
    if x2 < y2:
        return False

    if x3 < y3:
        return True
    else:
        return False


def insertionSort(l, nomes):
    for i in range(1, len(l)):
        prox = l[i]
        j = i - 1
        while j >= 0 and anterior(prox, l[j], nomes):
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = prox


def main():


if __name__ == '__main__':
    main()
