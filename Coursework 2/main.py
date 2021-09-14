import modulo


def main():
    modulo.verarquivo()
    print("Olá, Usuário! Por favor escolha umadas opções abaixo:\n"
          "     1) Cadastrar um novo motorista.\n"
          "     2) Cadastrar um novo veículo.\n"
          "     3) Alterar proprietário de um veículo.\n"
          "     4) Cadastrar uma nova infração.\n"
          "     5) Sair do sistema.")
    opcao = int(input())
    while opcao != 5:
        if opcao == 1:
            modulo.novomotorista()
        if opcao == 2:
            modulo.novoveiculo()
        if opcao == 3:
            modulo.alteraproprietario()
        if opcao == 4:
            modulo.novainfracao()
        print("     1) Cadastrar um novo motorista.\n"
              "     2) Cadastrar um novo veículo.\n"
              "     3) Alterar proprietário de um veículo.\n"
              "     4) Cadastrar uma nova infração.\n"
              "     5) Sair do sistema.")
        opcao = int(input())
    modulo.limpaTela()


if __name__ == '__main__':
    main()
