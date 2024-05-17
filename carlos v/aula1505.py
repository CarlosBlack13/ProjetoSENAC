'''
print("Cadastre aqui sua senha com os seguintes criétios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = str(input("Digite sua senha : "))

#validação

while senha.islower():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")
        print("Senha aceita")

while len(senha) < 7 :
    senha = input("A senha deve ter pelo menos 8 caracteres: ")
print("Senha aceita")

while senha.isalpha() :
    senha = input("Necessita de um numero: ")
    print("Senha aceita")

while senha.isalnum() :
    senha = input("Necessita de um Caractere especial: ")
    print("Senha aceita")
    '''


'''from pickletools import pystring


frase = input("Digite uma palavra: ")
contagem = 0
indice = -1

while True:
    indice = frase.find(pystring, indice + 1)
    if indice < 0:
        break
    contagem += 1

print(contagem)'''

    
'''frase = input("Digite uma palavra: ")
substring = "Python"
contagem = 0
indice = -1

while True:
    indice = frase.find(substring, indice + 1)
    if indice == -1:
        break
    contagem += 1

print(contagem) '''



'''from collections import Counter

texto = input("")
counter = Counter(texto)

print(counter)'''


'''def mettocent(met):
    cent = met * 100
    return cent

def centtomet(cent):
    met = cent / 100
    return met

def mettokil(met):
    kil = met / 1000
    return kil

def kiltomet(kil):
    met= kil * 1000
    return met

def centtokil(cent):
    kil = cent / 100000
    return kil

def kiltocent(kil):
    cent = kil * 100000
    return cent

escolha = True

while escolha == True:

    print('Escolha uma opção de conversão:')
    print('1 Metros para centimetros\n2 Centimetros para metros\n3 Metros para quilometros')
    print('4 Quilometros para metros\n5 Centimetros para quilometros\n6 Quilometros para centimetros\n')
    escolha = int(input())

    if escolha > 6:
        print("Opção inválida, digite novamente")
        continue

    dist = float(input("Digite a distância a ser convertida:"))

    if escolha == 1:
        print(mettocent(dist), "centimentros")
        break
    elif escolha == 2:
        print(centtomet(dist), "metros")
        break
    elif escolha == 3:
        print(mettokil(dist), "quilometros")
        break
    elif escolha == 4:
        print(kiltomet(dist), "metros")
        break
    elif escolha == 5:
        print(centtokil(dist), "quilometros")
        break
    elif escolha == 6:
        print(kiltocent(dist), "centimentros")
        break'''



    
    
    







    