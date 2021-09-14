import pickle
import os.path


def lerarquivo():
    with open("entrada.bin", "rb") as f:
        alunos = pickle.load(f)
        notas = pickle.load(f)
        f.close()
        return alunos, notas


def existeArquivo():
    if (os.path.isfile('entrada.bin')):
        return True
    else:
        print("O arquivo não existe")
        return False


# Função que realiza a soma dos itens das tuplas e retorna eles
def maiorSoma(esquerda, direita):
    somaEsquerda = 0
    somaDireita = 0
    for i in esquerda[1:5]:
        somaEsquerda = i + somaEsquerda
    for j in direita[1:5]:
        somaDireita = j + somaDireita
    return somaEsquerda, somaDireita


# Função que filtra os parametros de ordenação
def anterior(esquerda, direta, alunos):
    somaEsquerda, somaDireita = maiorSoma(esquerda, direta)

    # Avalia a soma da nota total
    if somaEsquerda > somaDireita:
        return True
    if somaEsquerda < somaDireita:
        return False

    # Caso a soma seja igual ele avalia a segunda nota
    if somaEsquerda == somaDireita:
        if esquerda[2] > direta[2]:
            return True
        if esquerda[2] < direta[2]:
            return False

    # Avalia o menor tempo de execução
    if esquerda[5] < direta[5]:
        return True
    if esquerda[5] > direta[5]:
        return False

    # Avalia a ordem alfabética
    if alunos[esquerda[0]] < alunos[direta[0]]:
        return True
    if alunos[esquerda[0]] > alunos[direta[0]]:
        return False


def merge(l, esquerda, direita, alunos):
    i, j, k = 0, 0, 0

    while i < len(esquerda) and j < len(direita):
        if anterior(esquerda[i], direita[j], alunos):
            l[k] = esquerda[i]
            i = i + 1
        else:
            l[k] = direita[j]
            j = j + 1
        k = k + 1

    while i < len(esquerda):
        l[k] = esquerda[i]
        i = i + 1
        k = k + 1

    while j < len(direita):
        l[k] = direita[j]
        j = j + 1
        k = k + 1


def mergeSort(l, alunos):
    if len(l) > 1:
        meio = len(l) // 2
        esquerda = l[:meio]
        direita = l[meio:]
        mergeSort(esquerda, alunos)
        mergeSort(direita, alunos)
        merge(l, esquerda, direita, alunos)

    return l

#  Função que avalia se o aluno recebe os dois pontos extras e mostra as notas.
def avalia2pts(l, alunos):
    cont = 0
    nota2 = l[4][2]
    tempo = l[4][5]
    for i in l:
        chave = i[0]
        soma = sum(i[1:5])
        if cont <= 5:
            soma = soma + 2
            cont = cont + 1
        if cont > 6:
            if i[2] == nota2 and i[5] == tempo:
                soma = soma + 2

        print(f"{alunos[chave]} {soma}")
