def k_multiplos():
    k = int(input("k: "))
    n = int(input("n: "))
    multiplos = []
    cont = 2
    for i in range(k):
        num = n*cont
        multiplos.append(num)
        cont = cont + 1
    print(multiplos)

if __name__ == '__main__':
    k_multiplos()
