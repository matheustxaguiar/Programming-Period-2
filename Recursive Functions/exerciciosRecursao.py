"""
# 1)
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


# 2)
def soma(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + soma(l[1:])


# 3)
def fibonacci(l):
    if l == 1:
        return 1
    if l == 2:
        return 1
    if l > 2:
        return fibonacci(l-2)+fibonacci(l-1)


# 4)
def exponencial(x, n):
    if n == 0:
        return 1
    else:
        return x * exponencial(x, n-1)


# 5)
def maior(x, y):
    if x > y:
        return x
    else:
        return y


def max(l):
    if len(l) == 1:
        return l[0]
    else:
        return maior(l[0], max(l[1:]))


def main():
    l = [1, 2, 3, 4, 5, 6]
    resultado = max(l)
    print(resultado)

if __name__ == '__main__':
    main()



# 7)
def inverte(x):
    if x // 10 == 0:
        print(x)
    else:
        print(x%10, end="")
        inverte(x//10)


def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(origem, "-> ", destino)
    else:
        hanoi(n-1, origem, auxiliar, destino)
        print(origem, "-> ", destino)
        hanoi(n-1, auxiliar, destino, origem)


def main():


if __name__ == '__main__':
    main()

"""
