import pickle
import os


def verarquivo():
    with open("multas.bin", "rb") as f:
        motoristas = pickle.load(f)
        veiculos = pickle.load(f)
        infracoes = pickle.load(f)
        naturezas = pickle.load(f)
        print(f"motoristas: {motoristas}")
        print(f"veiculos: {veiculos}")
        print(f"Infrações: {infracoes}")
        print(f"naturezas: {naturezas}")


def lerarquivo():
    with open("multas.bin", "rb") as f:
        motoristas = pickle.load(f)
        veiculos = pickle.load(f)
        infracoes = pickle.load(f)
        naturezas = pickle.load(f)
        f.close()
        return motoristas, veiculos, infracoes, naturezas


def escrevearquivo(motoristas, veiculos, infracoes, naturezas):
    with open("multas.bin", "wb") as file:
        pickle.dump(motoristas, file)
        pickle.dump(veiculos, file)
        pickle.dump(infracoes, file)
        pickle.dump(naturezas, file)
        file.close()


def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def novomotorista():
    limpaTela()
    print("Bem-vindo(a) ao Cadastro de Novo Motorista! 🚗 🚗 🚗\n")
    motoristas, veiculos, infracoes, naturezas = lerarquivo()
    print("Por favor, tenha sua CNH e identidade em mãos.\n")
    cnh = input("CNH: ")
    while cnh in motoristas:
        print("CNH já existente, insira outra.")
        cnh = input("CNH: ")
    nome = input("Nome: ")
    print("Data de Nascimento")
    nascimento = (int(input('dia: ')), int(input('mes: ')), int(input('ano: ')))
    motoristas[cnh] = (nome, nascimento)
    escrevearquivo(motoristas, veiculos, infracoes, naturezas)
    print("Cadastro Finalizado com sucesso! \n")


def novoveiculo():
    limpaTela()
    print("Bem-vindo(a) ao Cadastro de novo veiculo! 🚗 🚗 🚗\n")
    motoristas, veiculos, infracoes, naturezas = lerarquivo()
    print("Por favor, tenha sua CNH e documentos do veiculo em mãos.\n")
    placa = input("Placa do veiculo: ")
    while placa in veiculos:
        print("Placa já existente, insira outra.")
        placa = input("Nova placa: ")
    cnh = input("CNH: ")
    modelo = input("Modelo do veículo: ")
    cor = input("Cor do veículo: ")
    veiculos[placa] = (cnh, modelo, cor)
    escrevearquivo(motoristas, veiculos, infracoes, naturezas)
    print("Cadastro Finalizado com sucesso! \n")


def alteraproprietario():
    limpaTela()
    print("Bem-vindo(a) ao Alterar proprietario(a) 🚗 🚗 🚗 \n")
    motoristas, veiculos, infracoes, naturezas = lerarquivo()
    print("Tenha em mãos CNH e documentação do veículo.\n")
    placa = input("Placa do veiculo: ")
    cnh = input("CNH do novo proprietário: ")
    if cnh not in motoristas or placa not in veiculos:
        print("ERROR: CNH do motorista ou placa não estão cadastrados.\n")
    for chave in veiculos:
            if chave == placa:
                dados = veiculos[chave]
                modelo = dados[1]
                cor = dados[2]
                veiculos[chave] = (cnh, modelo, cor)
    escrevearquivo(motoristas, veiculos, infracoes, naturezas)
    print("Proprietario alterado com sucesso! \n")


def novainfracao():
    limpaTela()
    print("Bem-vindo(a) ao Cadastro de novas infrações 🖋️🖋️ 🖋️.\n  ")
    motoristas, veiculos, infracoes, naturezas = lerarquivo()
    identificador = int(len(infracoes) + 1)
    data = (int(input("Data da infração: \nDia: ")), int(input("Mês: ")), int(input("Ano: ")))
    placa = input("Placa do Veículo: ")
    opcao = int(input("digite 1 para infração leve\n"
                         "digite 2 para infração média\n"
                         "digite 3 para infração grave\n"
                         "digite 4 para infração gravíssima.\n"))
    natureza = ""
    if opcao == 1:
        natureza = "Leve"
    if opcao == 2:
        natureza = "Media"
    if opcao == 3:
        natureza = "Grave"
    if opcao == 4:
        natureza = "Gravissima"
    infracao = (identificador, data, placa, natureza)
    infracoes.append(infracao)
    escrevearquivo(motoristas, veiculos, infracoes, naturezas)
    print("Infração cadastrada com sucesso! \n")
