from boneco import exibir_boneco
from palavras import selecione_palavra

def play():
    palavra = selecione_palavra()
    palavra_completa = '_' * len(palavra)
    adivinhado = False
    letras_adivinhadas = []
    palavras_adivinhadas = []
    tentativas = 6

    print("Vamos jogar Jogo da Forca!")
    print(exibir_boneco(tentativas))
    print(palavra_completa)
    print("\n")

    while not adivinhado and tentativas > 0:
        palpite = input("Por favor adivinhe uma letra ou palavra: ").lower()
        if len(palpite) == 1 and palpite.isalpha():
            if palpite in letras_adivinhadas:
                print("Você já adivinhou a letra", palpite)
            elif palpite not in palavra:
                print(palpite, "não está na palavra.")
                tentativas -= 1
                letras_adivinhadas.append(palpite)
            else:
                print("Bom trabalho,", palpite, "está na palavra!")
                letras_adivinhadas.append(palpite)
                palavra_como_lista = list(palavra_completa)
                indices = [i for i, letra in enumerate(palavra) if letra == palpite]
                for indice in indices:
                    palavra_como_lista[indice] = palpite
                palavra_completa = ''.join(palavra_como_lista)
                if '_' not in palavra_completa:
                    adivinhado = True
        elif len(palpite) == len(palavra) and palpite.isalpha():
            if palpite in palavras_adivinhadas:
                print("Você já adivinhou a palavra", palpite)
            elif palpite != palavra:
                print(palpite, "não é a palavra.")
                tentativas -= 1
                palavras_adivinhadas.append(palpite)
            else:
                adivinhado = True
                palavra_completa = palavra
        else:
            print("Palpite inválido.")

        print(exibir_boneco(tentativas))
        print(palavra_completa)
        print("\n")

    if adivinhado:
        print("Parabéns, você adivinhou a palavra! Você ganhou!")
    else:
        print("Desculpe, você ficou sem tentativas. A palavra era " + palavra + ". Talvez da próxima vez!  ;-;")

if __name__ == "__main__":
    play()