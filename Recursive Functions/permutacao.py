def troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux


def perms(l, pos=0):
    if pos == len(l) - 1:
        print(l)
    else:
        for i in range(pos, len(l)):
            troca(l, pos, i)
            perms(l, pos+1)
            troca(l, pos, i)


def main():
    l = [1, 2, 3]
    perms(l)


if __name__ == '__main__':
    main()
