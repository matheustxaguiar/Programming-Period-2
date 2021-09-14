def salarios():
    n = int(input("n: "))
    nome = []
    salario = []
    for i in range(n):
        nome.append(str(input("Nome: ")))
        salario.append(float(input("Salário: ")))
    med = sum(salario)/n
    print(f"Media salarial: R${med}")
    for j in salario:
        if j > med:
            print(salario.index(j))
            funcionario = nome.pop(salario.index(j))
            nome.insert(salario.index(j), funcionario)
            print(f"O funcionário acima da média salarial é: {funcionario}")

if __name__ == '__main__':
    salarios()
