def ocorrencias():
    n = int(input("n: "))
    lista = []
    cont = 0
    for i in range(n):
        lista.append(input("Insira um número: "))
    num = input("Qual número deseja contar? ")
    for i in lista:
        if i == num:
            cont = cont + 1
    print(lista)
    print(f"o número {num} aparece {cont} vezes na lista.")

if __name__ == '__main__':
    ocorrencias()
