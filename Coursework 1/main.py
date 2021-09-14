from random import randint
import modulo


def main():
    print("Olá, usuário!")
    nome = str(input("Qual o seu nome?"))
    escolha = "s"
    maiorsecao = 0
    recordpts = modulo.verificaVazio()
    if recordpts != 0:
        record = modulo.lerDados(nome, maiorsecao)
        recordpts = int(record[1])
    while escolha == "s":
        sorteado = randint(0, 9)
        correta = [sorteado]
        x = []
        print("O primeiro numero sorteado foi:", sorteado)
        x.append(int(input("Digite a sequencia completa:")))
        while x == correta:
            sorteado = randint(0, 9)
            correta.append(sorteado)
            modulo.limpaTela()
            print(f"O novo número é {sorteado}")
            x = []
            x.append(int(input("Digite a sequencia completa: ")))
            x = modulo.listaNum(x.pop(0))
        pontos = len(correta)-1
        if pontos > maiorsecao:
            maiorsecao = pontos
            if maiorsecao > recordpts:
                modulo.armazenarDados(nome, maiorsecao)
        print("Errou! Você acertou: ", pontos, " números.")
        print(f"A maior pontuação alcançada na seção é: {maiorsecao} pts \n")
        record = modulo.lerDados(nome, maiorsecao)
        recordista = record[0]
        recordpts = int(record[1])
        print(f"｡☆✼★━━━━━━ Record ━━━━━━★✼☆｡")
        print(f"    ｡☆ {recordista} - {recordpts}pts ☆｡\n")
        print("    ──────▄▀▄─────▄▀▄\n"
              f"    ─────▄█░░▀▀▀▀▀░░█▄  tente novamente {nome}! \n"
              "    ─▄▄──█░░░░░░░░░░░█──▄▄\n"
              "    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n")
        escolha = str(input("Deseja continuar? Digite s ou n: "))
        modulo.limpaTela()


if __name__ == '__main__':
    main()
