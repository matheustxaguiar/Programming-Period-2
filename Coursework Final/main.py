import modulo


def main():
    if modulo.existeArquivo():
        alunos, notas = modulo.lerarquivo()
        ordem = modulo.mergeSort(notas, alunos)
        modulo.avalia2pts(ordem, alunos)
    else:
        print("Por favor insira o arquivo e rode o programa novamente.")


if __name__ == '__main__':
    main()
