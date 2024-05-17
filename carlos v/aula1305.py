'''import math

numero = 16
raiz_quadrada = math.sqrt(numero)
print("A raiz quadra de", numero "é: ",raiz_quadrada)'''

'''import random

numero_aleatorio = random.randint(1,100)
print("O numero aleatorio é: ", numero_aleatorio)

lista = [1, 2, 3, 4, 5]
embaralhe = random.shuffle(lista)
print("A lista embaralhada é: ", lista)'''

import random
import math

'''def jogoaleadorio():
    numerousuario = int(input("Digite um valor: "))
    numerosorteado = random.randint(1, 100)

def iniciar():
    quarda = numerousuario
    contador = 1
    while(numerousuario != quarda):
        if(numerousuario == quarda):
            print(f"Você acertou !! o numero é {quarda}")
            return
        elif(numerousuario < quarda):
            print("Este nume da frio")
            jogoaleadorio()
            contador += 1
        elif(numerousuario > quarda):
            print("Este nume da quende")
            jogoaleadorio()
            contador += 1'''


def jogo_adivinhacao():
    numero_aleadorio = random.randint(1,100)
    tentativas = 0

    while True:
        palpite = int(input("Tente adivinhar o número entre 1 e 100: "))
        tentativas += 1

        if palpite < numero_aleadorio:
            print("Numero baixo. Tente novamente.")
        elif palpite > numero_aleadorio:
            print("Numero alto. Tente novamente.")
        else:
            print(f"Parabéns !! Você acertou o número{numero_aleadorio}")
            break

jogo_adivinhacao()


