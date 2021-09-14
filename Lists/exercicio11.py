def media():
    n = int(input("n: "))
    if n <= 0 or n > 100:
        print("Insira um valor maior que 0 e menor ou igual a 100.")
    else:
        lista = []
        cont = 0
        for i in range(n):
            lista.append(int(input("nota: ")))
        md = sum(lista) / n
        print(f"A média é: {md}")
        for j in lista:
            if j >= 60:
                cont = cont + 1
        print(f"O número de alunos que ficaram acima da média é: {cont}")


if __name__ == '__main__':
    media()


"""
    lista = []
    n = int(input("n: "))
    cont = 0
    if 100 >= n > 0:  # n <= 100 and n > 0:
        for i in range(n):
            nota = int(input("nota: "))
            lista.append(nota)
            if nota >= 60:
                cont = cont + 1
        med = (sum(lista)) / n
        print(f"A media de todas as notas é: {med}")
        print(f"{cont} alunos ficaram acima de  60 pontos.")
    else:
        print("Insira um número inteiro entre 0 e 100.")

"""