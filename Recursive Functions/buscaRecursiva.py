#  Busca de forma recursiva:

def buscaPosRec(x, l, pos=0):
    if pos == len(l):
        return -1
    else:
        if l[pos] == x:
            print(f"Encontrei está na posição: {pos}")
            return pos
        else:
            buscaPosRec(x, l, pos+1)


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    buscaPosRec(7, l)


if __name__ == '__main__':
    main()
