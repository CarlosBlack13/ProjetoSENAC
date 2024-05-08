'''def fatorial(a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in  range (1, a+1):
            fat *= i
        return fat
    
    
x = int(input ("Digite um número intero: ") )

print("o fatorial de", x, "é: ", fatorial(x))'''


'''a = input ("Digite seu nome: ")
b = int(input ("Digite sua idade: "))
c = float(input ("Digite sua altura: "))
tem_carro = input("Você possui algum carro? (sim/não): ")

tem_carro = tem_carro.lower() == "sim"

print("Informaçãoes digitadas: ")
print("a", a)
print("b", b)
print("c", c)
print("tem carro?", "sim" if tem_carro else "não")'''

'''def contagem_regressiva():
    numero = int(input ("Digite um número intero positivo: "))
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
        contagem_regressiva()

    else:
        while numero >=0:
            print(numero)
            numero -= 1
    
contagem_regressiva()'''


def soma (o , i):
     return  o + i
     
def subtracao ( o ,i):
     return  o - i 
      
     
def multiplicacao (o, i):
       return  o * i
       
       
def divisao  (o, i):
        if i != 0: 
          return  o / i 
        else:
             return "Divisão invalida"
 
def calculadora():
     print("Bem-vindo a calauladora em python !")
     print("Selecione a operação")
     print("1: soma")
     print("2: subtração")
     print("3: multiplicação")
     print("4: divisão")

    
     escolha = input("Digite sua escolha 1/2/3/4: ")

    if escolha in ('1', '2', '3', '4'):
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))

            
        if escolha == '1':
                print("Resultado", soma(num1, num2))
            elif escolha == '2':
                print("Resultado", subtracao(num1, num2))
            elif escolha == '3':
                print("Resultado", multiplicacao(num1, num2))
            elif escolha == '4':
                print("Resultado", divisao(num1, num2))
        

        elif:
                print("Escolha Invalida.")

calculadora()

        


