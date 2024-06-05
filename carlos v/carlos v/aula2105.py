'''class Pessoa:
    def __init__(self , nome, idade, pesso, altura):
        self.nome = nome
        self.idade = idade
        self.pesso = pesso
        self. altura =altura

        p1 = Pessoa("John", 36, 80, 1.70)

print(p1) # type: ignore'''


class Person:
  def __init__(self, name, idade, pesso, altura):
    self.name = name
    self.idade = idade
    self.pesso = pesso
    self.altura = altura
  def envelhecer(self):
    self.idade += 1
    if self.idade < 21:
      self.crescar(0.5)

  def engordar (self, pesso):
    self.pesso += pesso

    
  def __str__(self):
    return f"Nome: {self.name}\nIdade: {self.idade}\nPesso: {self.pesso}\nAltura: {self.altura}"


p1 = Person("victor", 18, 80, 1.66)

print(p1)