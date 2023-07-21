import random
import string

def gerarStringAleatoria(tamanho, incluirCaracteresEspeciais):
    caracteres = string.ascii_letters + string.digits
    if incluirCaracteresEspeciais:
        caracteres += "!@#$%&*()"

    resultado = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return resultado

gerarNovamente = True

while gerarNovamente:
    tamanho = int(input("Digite o tamanho da string: "))
    incluirCaracteresEspeciais = bool(int(input("Incluir caracteres especiais (!@#$%&*)? (1 = Sim, 0 = Não): ")))

    senha = gerarStringAleatoria(tamanho, incluirCaracteresEspeciais)
    print("Senha gerada:", senha)

    resposta = int(input("Deseja gerar outra senha? (1 = Sim, 0 = Não): "))
    gerarNovamente = (resposta == 1)
