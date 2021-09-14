import os


def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def listaNum(x):
    num = x
    quo = num
    lista = []
    while quo != 0:
        rest = num % 10
        quo = num//10
        num = quo
        lista.append(rest)
    return lista[::-1]


def armazenarDados(nome, maiorsecao):
    f = open("dados.txt", "wt")
    f.write(nome + "\n")
    f.write(str(maiorsecao))
    f.close()


def lerDados(nome, maiorsecao):
    with open("dados.txt", "r") as arq:
        x = arq.read()
        y = x.split()
        return y


def verificaVazio():
    with open('dados.txt') as my_file:
        my_file.seek(0)
        first_char = my_file.read(1)
        if not first_char:
            recordpts = 0
            return recordpts
