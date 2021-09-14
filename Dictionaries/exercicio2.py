"""
Agenda: Faca um programa no qual o usuario possa armazenar o numero detelefone de quantos contatos ele quiser.
O programa tem um menu com duas opcoes:
    Cadastrar telefone: Usu ́ario digita nome e telefone de um novo contato.
    Visualizar agenda: Programa exibe nomes e telefones cadastrados.
"""
agenda = {}
print("a)Cadastrar telefone.")
print("b)Visualizar agenda.")
opcao = input("escolha uma opção: ")


while opcao == "a":
    telefone = int(input("telefone: "))
    contato = input("contato: ")
    agenda[telefone] = contato
    print("a)Cadastrar telefone.")
    print("b)Visualizar agenda.")
    opcao = input("escolha uma opção: ")

for key in agenda:
    print(f"{agenda[key]}:{key}")
