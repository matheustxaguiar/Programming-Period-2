def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = int(input("n: "))
    soma = fib(n)
    print(soma)


if __name__ == '__main__':
    main()
