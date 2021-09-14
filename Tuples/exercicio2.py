"""
Agora, a mesma empresa deseja saber se seus produtos estao dando lucro. Para isso,pediu para voce criar uma sub-rotina
que recebe uma lista de tuplas contendo o pre code custo e o preco de venda de cada mercadoria e imprima:

A) a quantidade de produtos com menos de 20% de lucro.
B) a porcentagem de produtos com lucro superior a 25%.
"""


def lucro():
    lista = [(5, 10), (2, 3), (88, 100)]
    menos20 = 0
    mais25 = 0

    for (custo, venda) in lista:
        if ((venda-custo)/custo) < 0.2:
            menos20 = menos20 + 1
        if ((venda-custo)/custo) > 0.25:
            mais25 = mais25 + 1
    print(f"A quantidade de produtos com menos de 20% de lucro é: {menos20}")
    print(f"A porcentagem de produtos com mais de 25% é: {mais25/len(lista)}%")


if __name__ == '__main__':
    lucro()
