
import random
lista_random = []


def gerar_lista():
    while True:
        try:
            quantidade = int(input('Informe quantos números:  '))
            valor_minimo = int(input('Informe o valor inicial:'))
            valor_maximo = int(input('Informe o  valor final: '))

        except ValueError:
            print('Valor errado')
        else:
            while True:
                lista_random.append(random.randint(valor_minimo, valor_maximo))
                if len(lista_random) == quantidade:
                    print(True)
                    return(lista_random)
        finally:

            if len(lista_random) == quantidade:

                print(f'{lista_random}\n')
                return True
            else:
                print(None)
                return False


gerar_lista()
