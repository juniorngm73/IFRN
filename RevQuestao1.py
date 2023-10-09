# Gerando e Salvando a lista com 02 funções no mesmo código.
import os
import random

def gerar_lista():
    while True:
        try:
            quantidade = int(input('Informe quantos números:  '))
            valor_minimo = int(input('Informe o valor inicial: '))
            valor_maximo = int(input('Informe o valor final: '))

# Gerar  lista aleatória.
            lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]

            if len(lista) > 0:
                print (True)

# Imprimir lista, sendo um numero em cada linha.
            for numero in lista:
                print(numero)

# Retorna a lista gerada
            return lista

        except ValueError:
            print("Valor inválido. Tente novamente.")



def salvar_lista(nome_lista, nome_arquivo):
    file = open(f'{nome_arquivo}.txt', 'w')

# Escrever lista no Arquivo, sendo um numero em cada linha.
    for i in nome_lista:
        file.writelines(f'{i}\n')
    file.close()
    print(os.path.exists(f'./{nome_arquivo}.txt'))

# Gera o Arquivo lista_random.txt

lista_gerada = gerar_lista()
salvar_lista(lista_gerada, 'treino')


