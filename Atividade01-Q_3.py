import random

def carregar_palavras(atividade1):

  palavras = []
  with open(atividade1, 'r') as arquivo:
    for linha in arquivo:
      palavra = linha.strip()
      if 5 <= len(palavra) <= 8:
        palavras.append(palavra)
  return palavras


def sortear_palavra(lista_palavras):

  palavra_sorteada = random.choice(lista_palavras)
  return palavra_sorteada


def verificar_palavra(arquivo, palavra_secreta):
    resultado = []
    for i in range(len(palavra_secreta)):
        if arquivo[i] == palavra_secreta[i]:
            resultado.append('🟩')  # Verde para letra certa na posição certa
        elif arquivo[i] in palavra_secreta:
            resultado.append('🟨')  # Amarelo para letra certa na posição errada
        else:
            resultado.append('⬜')  # Cinza para letra errada
    return ''.join(resultado)


def jogar():

    for tentativa in range(6):
        palavra_usuario = input(f"Tentativa {tentativa+1}: ").upper()
        if len(palavra_usuario) != len(palavra_secreta):
            print("A palavra deve ter o mesmo número de letras.")
            continue

        if resultado == '🟩' * len(palavra_secreta):
            print("Parabéns, você acertou!")
            return
    print(f"Você perdeu. A palavra era: {palavra_secreta}")




arquivo = 'atividade1.txt'
lista_palavras = carregar_palavras(arquivo)
palavra_secreta = sortear_palavra(lista_palavras)
resultado = verificar_palavra(arquivo, palavra_secreta)
#print(resultado)
#print(palavra_secreta)


# Iniciar o jogo
if __name__ == "__main__":
    jogar()