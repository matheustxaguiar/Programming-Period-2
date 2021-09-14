def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return f"Lista ordenada: {l}"


def main():
    l = [3, 2, 1, 4, 9, 10, 2, 3]
    print(l)
    resultado = bubbleSort(l)
    print(resultado)

if __name__ == '__main__':
    main()
