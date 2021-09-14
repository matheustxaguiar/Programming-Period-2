def fat(n):
    if n > 0:
        return n * fat(n-1)
    else:
        return 1


def main():
    n = int(input("n: "))
    fatorial = fat(n)
    print(fatorial)


if __name__ == '__main__':
    main()
