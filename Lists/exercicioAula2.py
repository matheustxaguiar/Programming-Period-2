def repeticao(alice, beatriz):
    l1 = []
    l2 = []
    for i in alice:
        if i not in l1:
            l1.append(i)
    for j in beatriz:
        if j not in l2:
            l2.append(j)
    return l1, l2


def troca():
    alice = [1, 1, 2, 3, 5, 7, 8, 8, 9, 15]
    beatriz = [2, 2, 2, 3, 4, 6, 10, 11, 11]
    ca = 0
    cb = 0
    a, b = repeticao(alice, beatriz)
    for i in a:
        if i not in b:
            ca = ca + 1
    for j in b:
        if j not in a:
            cb = cb + 1
    print(f"O valor máximo de caretas que podem ser trocadas é: {min(ca, cb)}")


if __name__ == '__main__':
    troca()
