"""
Adultos: Crie um dicionario com nome, idade e telefone de 10 pessoas (os dadosserao digitados pelo usuario).
Depois, remova todos os usuarios que forem menoresde idade, e imprima nome/telefone dos que permanecerem.
            #Telefone  Idade  Nome
adultos = {998556878: [36, "Marcos"],
           983865594: [55, "José"],
           999861821: [16, "Felipe"],
           991226368: [17, "Leonardo"],
           993190759: [15, "Maria"],
           989189362: [88, "Roberval"],
           991924550: [101, "Clotilde"],
           995704780: [70, "Ana Maria"],
           997395232: [13, "Enzo"],
           988988443: [55, "Cornelios"]}
"""
geral = {}
adultos = {}

for i in range(10):
    nome = input("Nome: ")
    telefone = int(input("Telefone: "))
    idade = int(input("Idade: "))
    geral[telefone] = [idade, nome]


for key in geral:
    if geral[key][0] >= 18:
        adultos[key] = geral[key]
for i in adultos:
    print(adultos[i])
