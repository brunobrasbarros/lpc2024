import random

print(('=' * 20), "SEJA BEM VINDO AO JOGO DA FORCA!", ('=' * 20))

chutes = 0
limite_chutes = 6
chutes_errados = []
chutes_adivinhados = []

with open('palavras.txt', 'r') as ListaDePalavras:

    palavras = ListaDePalavras.read().splitlines()
    escolha = random.choice(palavras).lower().strip()
    tamanho = len(escolha)
    PalavraEscolhida = ['_'] * tamanho

while chutes < limite_chutes:

    print("ADIVINHE A SEGUINTE PALAVRA:", ' '.join(PalavraEscolhida))
    chute = input("ESCREVA UMA LETRA: ").lower()

    if chute in chutes_adivinhados or chute in chutes_errados:
        print("OPA! Parece que você já testou essa letra, tente novamente.")
        continue

    if len(chute) > 1:
        print("opa! uma só letra")
        continue

    if len(chute) < 1:
        print("opa! escreva alguma coisa")
        continue

    if not chute.isalpha():
        print("opa! Somente letras")
        continue

    if chute in escolha:
        for i in range(tamanho):
            if chute == escolha[i]:
                PalavraEscolhida[i] = chute
        chutes_adivinhados.append(chute)

    else:
        chutes += 1
        chutes_errados.append(chute)
        print(f"{chutes} chutes errados")

    if '_' not in PalavraEscolhida:
        print(f"VOCÊ ADIVINHOU A PALAVRA '{escolha.upper()}', PARABÉNS!")
        break

else:
    print(f"Você perdeu e foi brutalmente enforcado. "
          f"A palavra era '{escolha.upper()}'.")

