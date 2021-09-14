def insertionSort(l):
    for k in range(1, len(l)):
        elem = l[k]
        pos = k-1

        while pos >= 0 and l[pos] > elem:
            l[pos+1] = l[pos]
            pos = pos - 1

        l[pos+1] = elem
    return l


def main():
    l = [2, 3, 1, 11, 6, 10]
    result = insertionSort(l)
    print(result)


if __name__ == '__main__':
    main()
