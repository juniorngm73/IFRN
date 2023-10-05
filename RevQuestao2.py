def ler_arquivo():
    nome_arquivo = input('Digite o Arquivo a ser Lido : ')
    arquivo = open(f'{nome_arquivo}.txt', 'r')
    conteudo = arquivo.read()



    print(conteudo)

    arquivo.close()



ler_arquivo()