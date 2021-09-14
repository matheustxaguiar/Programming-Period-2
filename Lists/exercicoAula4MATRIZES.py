""" Um professor deseja calcular a média de notas de uma turma. Faça um procedimento que leia um amtriz contendo as
notas dos alunos. O procedimento começa perguntando ao usuário o número m de alunos e o número n de notas de cada um
dos m alunos. O procedimento deve imprimir a nota de cada aluno e a média geral da turma. A nota final de cada aluno é
a média simples das suas notas."""


def lernotas(m, n):
    alunos = []
    for i in range(m):
        notas = []

        for j in range(n):
            nota = int(input(f"Insira a nota {j+1} do aluno {i+1}: "))
            notas.append(nota)
        alunos.append(notas)

    return alunos


def main():
    m = int(input("Número de alunos: "))
    n = int(input("Número de avaliações: "))

    alunos = lernotas(m, n)
    stotal = 0
    for i in alunos:
        soma = 0
        for j in i:
            soma = j + soma
        media = soma/len(i)
        stotal = media + stotal
        print(f"Aluno {int(alunos.index(i))+1}: Nota {media} pts")
    mediatotal = stotal/m
    print(f"A média total de notas é: {mediatotal}")


if __name__ == '__main__':
    main()
