'''valor1 = int(input("Digite cinco números:"))
valor2 = int(input("Digite cinco números:"))
valor3 = int(input("Digite cinco números:"))
valor4 = int(input("Digite cinco números:"))
valor5 = int(input("Digite cinco números:"))

media = float((valor1+valor2+valor3+valor4+valor5)/5)
print(media)'''

input("Escreva uma palavra:")
def conta_vogais(string):
    vogais = 'aeiou'
    contador = 0
    for letra in string.lower():
        if letra in vogais:
            contador += 1
    return contador

print()

