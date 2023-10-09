
import os
def ler_arquivo():
    while True:
        try:

            nome_arquivo = input('Digite o Arquivo a ser Lido : ')
            arquivo = open(f'{nome_arquivo}.txt', 'r')
            conteudo = arquivo.read()

            print(os.path.exists(f'./{nome_arquivo}.txt'))

            print(conteudo)

            break
            arquivo.closecu()

        except:
            print(False)
            print('Arquivo não Encontrado, tente novamente')



ler_arquivo()